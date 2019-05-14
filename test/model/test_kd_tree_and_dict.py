import numpy as np
import pytest
from numpy import linalg

from src.model.ant import Ant
from src.model.food import Food
from src.model.game_object import GameObject
from src.model.kd_tree_and_dict import KdTreeAndDict
from src.model.nest import Nest
from src.model.world import World

from src.utils import array, randint

def array_in_list(position, position_list):
    """Helper function used for testing if a certain position (of type np.array) is in a list of positions"""
    return any((position == x).all() for x in position_list)


def array_remove_from_list(position, position_list):
    """Helper function used for testing if a certain position (of type array) is in a list of positions"""
    return [x for x in position_list if not (x == position).all()]


def test__init__():
    """Tests id creation of Kd_tre_and_dict works as expected."""
    tree = KdTreeAndDict()
    assert (issubclass(type(tree), World))
    assert (type(tree.all_objects) == dict)
    assert (len(tree.all_objects.values()) == 0)


# TODO: also random set ups
@pytest.fixture
def set_up_tree_nests_fixed():
    tree = KdTreeAndDict()
    # TOD0: Should trees assert that there are no two nests at one position?
    # Answer: I don't think so, such checks should be handled by the Controller (for our project at least)
    positions = [array([5, 5]), array([-5, -5])]
    colors = ['red', 'green']
    tree.create_nests(colors, positions, size=1, health=100)

    return tree, positions


# TODO also test for multiple things at a single location: In that case k nearest will give more then k GameObjects.
#  Decinde on who handles that case (Caller or world-function)?
@pytest.fixture
def set_up_food_fixed(set_up_tree_nests_fixed):
    """Sets up food.
    Please never remove positions and when adding, add to positions far away from existing ones.
    Other wise you might mess up other tests"""
    tree, nest_positions = set_up_tree_nests_fixed

    small_grid = [array([-1, -1]), array([-1, 0]), array([0, -1]), array([0, 0]), array([0, 1]),
                  array([1, 0]), array([1, 1]), array([-1, 1]), array([1, -1])]
    another_small_grid = [array([8, 8]), array([8, 9]), array([9, 8]), array([9, 9]), array([9, 10]),
                          array([10, 9]), array([10, 10]), array([8, 10]), array([10, 8])]
    yet_another_small_grid = [array([-8, -8]), array([-8, -9]), array([-9, -8]), array([-9, -9]),
                              array([-9, -10]), array([-10, -9]), array([-10, -10]), array([-8, -10]),
                              array([-10, -8])]
    food_grid_info = [((-1, 1), (1, -1), (0, 0), 1), ((8, 10), (10, 8), (9, 9), 1),
                      ((-10, -8), (-8, -10), (-9, -9), 1)]

    stacked_food = [array([-100, -100]), array([-100, -100]), array([-100, -100])]

    all_food_position_lists = [small_grid, another_small_grid, yet_another_small_grid, stacked_food]
    food_positions = [position for sublist in all_food_position_lists for position in sublist]
    sizes = [1] * len(food_positions)
    tree.create_food(food_positions, sizes)
    all_positions_flat = nest_positions.copy()
    all_positions_flat.extend(food_positions)

    all_positions = {"all positions": all_positions_flat,
                     "nests": nest_positions,
                     "nested food": all_food_position_lists,
                     "flat food": food_positions,
                     "food grid info": food_grid_info}
    return tree, all_positions


# TODO update as fixtures are extended
def test_dump_content(set_up_food_fixed):
    tree, positions = set_up_food_fixed
    all_objects = tree.dump_content()
    all_positions = positions["all positions"]
    all_nests = positions["nests"]
    all_food = positions["flat food"]
    for obj in all_objects:
        assert (array_in_list(obj.position, all_positions))
        if type(obj) == Food:
            assert (array_in_list(obj.position, all_food))
        elif type(obj) == Nest:
            assert (array_in_list(obj.position, all_nests))

    dumped_positions = [obj.position for obj in all_objects]
    for position in all_positions:
        assert (array_in_list(position, dumped_positions))


def test_get_at_position(set_up_food_fixed, position=array([-100, -100]), compare_to_index=3):
    tree, positions = set_up_food_fixed
    obj_list = tree.get_at_position(position)
    obj_positions = [obj.position for obj in obj_list]
    for obj_position in obj_positions:
        assert ((obj_position == position).all())
    assert (obj_positions == positions["nested food"][compare_to_index])


def test_create_ants(set_up_tree_nests_fixed):
    """Tests whether right amount of ants with type ant are created at nest positions."""
    tree, positions = set_up_tree_nests_fixed
    amount_ants = randint(1, 6)

    for pos in positions:
        nest = tree.get_at_position(pos)[0]
        tree.create_ants(nest, amount_ants)

    for pos in positions:
        objects_at_pos = tree.get_at_position(pos)
        assert len(objects_at_pos) == amount_ants + 1
        assert sum([isinstance(obj, Ant) for obj in objects_at_pos]) == amount_ants


def test_create_nests(set_up_tree_nests_fixed):
    """Test whether only one nest with type nest is created at the positions."""
    tree, positions = set_up_tree_nests_fixed

    for pos in positions:
        objects_at_pos = tree.get_at_position(pos)
        assert len(objects_at_pos) == 1
        assert isinstance(objects_at_pos[0], Nest)


def test_get_k_nearest(set_up_food_fixed, center_position=array([0, 0]), almost_center_pos=array([0.1, 0.1]),
                       nested_food_ind=0,
                       k_greater_1=4):
    """Tests for fixed data whether k-nearest objects are returned using the 'small_grid' in the 'set_up_food_fixed'
    fixture.
    The optional parameters are resent because I think they might enable simpler randomized testing."""
    tree, positions_dict = set_up_food_fixed

    # k = 1
    nearest_obj, dist = tree.get_k_nearest(center_position, 1)
    for obj in nearest_obj:
        assert (issubclass(type(obj), GameObject))
        assert ((obj.position == center_position).all())
    nearest_obj, dist = tree.get_k_nearest(almost_center_pos, 1)
    for obj in nearest_obj:
        assert (issubclass(type(obj), GameObject))
        assert ((obj.position == center_position).any())

    # k > 1
    actual_positions = positions_dict["nested food"][nested_food_ind]
    original_len = len(actual_positions)
    nearest_objs, dists = tree.get_k_nearest(center_position, k_greater_1)
    max_norm = 0
    for obj in nearest_objs:
        assert (issubclass(type(obj), GameObject))
        position = obj.position
        dist_form_center = linalg.norm(array(position) - array(center_position))
        if dist_form_center > max_norm:
            max_norm = dist_form_center
        assert (array_in_list(position, actual_positions))
        actual_positions = array_remove_from_list(position, actual_positions)
    assert (not array_in_list(center_position, actual_positions))
    assert (original_len - k_greater_1 == len(actual_positions))
    for far_away_position in actual_positions:
        dist = linalg.norm(array(far_away_position) - array(center_position))
        assert (dist >= max_norm)


def test_get_k_nearest_list(set_up_food_fixed, position_list=(array([-9, -9]), array([0, 0]), array([9, 9]))):
    """Tests the get_k_nearest_list() function and calls compares by comparing to multiple get_k_nearest() calls"""
    tree, positions_dict = set_up_food_fixed
    position_list = list(position_list)
    # k >= 1
    for k in range(5):
        nearest_objects, dists = tree.get_k_nearest_list(position_list, k + 1)
        for i, obj_list in enumerate(nearest_objects):
            compare_to_obj, compare_to_dists = tree.get_k_nearest(position_list[i], k + 1)
            assert (obj_list == compare_to_obj)
            assert ((dists[i] == compare_to_dists).any())


def test_get_square_region(set_up_food_fixed, food_grid_indices=range(3)):
    tree, positions_dict = set_up_food_fixed
    food_grids = []
    for idx in food_grid_indices:
        food_grids.append(positions_dict["nested food"][idx])
    grid_info = positions_dict["food grid info"]

    # See if all points in 2x2 grids are found by the function
    for i, grid in enumerate(food_grids):
        center = grid_info[i][2]
        radius = grid_info[i][3]
        objects = tree.get_square_region(center, radius)
        points = [obj.position for obj in objects]
        compare_to_points = food_grids[i]
        for point in points:
            assert (array_in_list(point, compare_to_points))
        for point in compare_to_points:
            assert (array_in_list(point, points))

    # See if for a smaller radius only center point is found
    for i, grid in enumerate(food_grids):
        center = grid_info[i][2]
        radius = grid_info[i][3]
        objects = tree.get_square_region(center, radius - radius / 1.1)
        points = [obj.position for obj in objects]
        assert (len(points) == 1)
        assert ((points[0] == center).all())


def test_get_rectangle_region(set_up_food_fixed, food_grid_indices=range(3)):
    tree, positions_dict = set_up_food_fixed
    food_grids = []
    for idx in food_grid_indices:
        food_grids.append(positions_dict["nested food"][idx])
    grid_info = positions_dict["food grid info"]

    for i, grid in enumerate(food_grids):
        top_left_square = grid_info[i][0]
        top_left_rectangle = array([top_left_square[0], top_left_square[1] - 0.5])
        bottom_right = grid_info[i][1]
        objects = tree.get_rectangle_region(top_left_rectangle, bottom_right)
        positions = [obj.position for obj in objects]
        for position in positions:
            assert (array_in_list(position, grid))

        for point in grid:
            if point[1] > top_left_rectangle[1]:
                assert (not array_in_list(point, positions))
            else:
                assert (array_in_list(point, positions))
