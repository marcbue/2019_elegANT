from src.model.kd_tree_and_dict import KdTreeAndDict
from src.model.nest import Nest

import pytest

@pytest.fixture
def set_up_tree_with_nests():
    tree = KdTreeAndDict()
    # TODO: can also be random parameters
    positions = [(0, 0), (-1, -1)]
    tree.create_nests(['red', 'green'], positions, size=1, health=100)
    return tree, positions

def test_get_position_2(set_up_tree_with_nests):
    tree, positions = set_up_tree_with_nests
    for pos in positions:
        objects_at_pos = tree.get_at_position(pos)

        # TODO: Yes, there can be several test made out of this.
        # There should be only 1 nest at a position.
        assert len(objects_at_pos) == 1
        assert isinstance(objects_at_pos[0], Nest)