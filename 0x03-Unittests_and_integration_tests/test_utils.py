#!/usr/bin/env python3
""" module to test utils file functions """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Sequence, Mapping, Any


class TestAccessNestedMap(unittest.TestCase):
    """class of unittest to test all function of utlis module """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, res: Any) -> None:
        """ unittest for access nested map function
            using parametrized method
        """
        function_res: Any = access_nested_map(nested_map, path)
        self.assertEqual(function_res, res)


if __name__ == '__main__':
    unittest.main()
