
from lesson001 import sort__the_jake_freestyle_method


class TestSorting(object):

    def test_sort__the_jake_freestyle_method(self):
        items = [-1, 5, 6, 3, 3, 4]

        sorted_items = sort__the_jake_freestyle_method(items)

        assert sorted_items == [-1, 3, 3, 4, 5, 6]
