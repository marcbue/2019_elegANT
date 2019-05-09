from src.model.kd_tree_and_dict import KdTreeAndDict
from src.model.nest import Nest
from src.model.ant import Ant

import pytest
import numpy as np

# TODO: also random set ups
@pytest.fixture
def set_up_tree_nests_fixed():
    tree = KdTreeAndDict()
    # TOD0: Should trees assert that there are no two nests at one position?
    positions = [(0, 0), (-1, -1)]
    colors = ['red', 'green']
    tree.create_nests(colors, positions, size=1, health=100)

    return tree, positions

@pytest.fixture
def set_up_food_fixed(set_up_tree_nests_fixed):
    tree, positions = set_up_tree_nests_fixed
    positions = [(-2, -2), (5, 2)]
    sizes = [1, 1]
    tree.create_food(positions, sizes)
    positions.append(positions)

    return tree, positions

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

def test_get_k_nearest(set_up_food_fixed):
    """Tests for fixed data whether k-nearest object is returned (k = 1)."""
    tree, positions = set_up_food_fixed
    nearest_obj, dist = tree.get_k_nearest((-5, -3), 1)

    # TODO.
    ### This should be an object! ###
    print(nearest_obj)