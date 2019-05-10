from src.model.kd_tree_and_dict import KdTreeAndDict
from src.model.nest import Nest
from src.model.ant import Ant
from src.model.game_object import GameObject

import pytest
import numpy as np
from numpy import linalg

# TODO: also random set ups
@pytest.fixture
def set_up_tree_nests_fixed():
    tree = KdTreeAndDict()
    # TOD0: Should trees assert that there are no two nests at one position?
    # Answer: I don't think so, such checks should be handled by the Controller (for our project at least)
    positions = [(5, 5), (-5, -5)]
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
    small_grid = [(-1, -1), (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]
    another_small_grid = [(8, 8), (8, 9), (9, 8), (9, 9), (9, 10), (10, 9), (10, 10), (8, 10), (10, 8)]
    yet_another_small_grid = [(-8, -8), (-8, -9), (-9, -8), (-9, -9),
                              (-9, -10), (-10, -9), (-10, -10), (-8, -10), (-10, -8)]
    all_position_lists = [small_grid, another_small_grid, yet_another_small_grid]
    positions = [position for sublist in all_position_lists for position in sublist]
    sizes = [1]*len(positions)
    tree.create_food(positions, sizes)

    all_positions = {"all positions": nest_positions.extend(positions),
                     "nests": nest_positions,
                     "nested food": all_position_lists,
                     "flat food": positions}
    return tree, all_positions


def test_create_ants(set_up_tree_nests_fixed):
    """Tests whether right amount of ants with type ant are created at nest positions."""
    tree, positions = set_up_tree_nests_fixed
    amount_ants = np.random.randint(1, 6)

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


def test_get_k_nearest(set_up_food_fixed, center_position=(0, 0), almost_center_pos=(0.1, 0.1), nested_food_ind=0,
                       k_greater_1=4):
    """Tests for fixed data whether k-nearest objects are returned using the 'small_grid' in the 'set_up_food_fixed'
    fixture.
    The optional parameters are resent because I think they might enable simpler randomized testing."""
    tree, positions_dict = set_up_food_fixed

    # k = 1
    nearest_obj, dist = tree.get_k_nearest(center_position, 1)
    for obj in nearest_obj:
        assert(issubclass(type(obj), GameObject))
        assert(obj.position == center_position)
    if(almost_center_pos):
        nearest_obj, dist = tree.get_k_nearest(almost_center_pos, 1)
        for obj in nearest_obj:
            assert(issubclass(type(obj), GameObject))
            assert(obj.position == center_position)

    # k > 1
    actual_positions = positions_dict["nested food"][nested_food_ind]
    original_len = len(actual_positions)
    nearest_objs, dists = tree.get_k_nearest(center_position, k_greater_1)
    max_norm = 0
    for obj in nearest_objs:
        assert(issubclass(type(obj), GameObject))
        position = obj.position
        dist_form_center = linalg.norm(np.array(position) - np.array(center_position))
        if dist_form_center > max_norm:
            max_norm = dist_form_center
        assert(position in actual_positions)
        actual_positions.remove(position)
    assert(not (center_position in actual_positions))
    assert(original_len - k_greater_1 == len(actual_positions))
    for far_away_position in actual_positions:
        dist = linalg.norm(np.array(far_away_position) - np.array(center_position))
        assert(dist >= max_norm)


def test_get_k_nearest_list(set_up_food_fixed, position_list = ((-9, -9), (0, 0), (9, 9))):
    """Tests the get_k_nearest_list() function and calls compares by comparing to multiple get_k_nearest() calls"""
    tree, positions_dict = set_up_food_fixed
    position_list = list(position_list)
    # k >= 1
    for k in range(5):
        nearest_objects, dists = tree.get_k_nearest_list(position_list, k+1)
        for i, obj_list in enumerate(nearest_objects):
            compare_to_obj, compare_to_dists = tree.get_k_nearest(position_list[i], k+1)
            assert(obj_list == compare_to_obj)
            assert ((dists[i] == compare_to_dists).any())
