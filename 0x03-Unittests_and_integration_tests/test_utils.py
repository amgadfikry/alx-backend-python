#!/usr/bin/env python3
""" module to test utils file functions """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Sequence, Mapping, Any, Type, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """class of unittest to test access nested map
        function of utlis module
    """
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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence,
            excp: Type[BaseException]) -> None:
        """ method to test access nested map function exception"""
        with self.assertRaises(excp):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ class of unittest to test get json
        function of utlis module
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(
            self, url: str, load: Dict, mock_get: Mock) -> None:
        """ methode using mock to test get json function """
        mock_res: Mock = Mock()
        mock_res.json.return_value = load
        mock_get.return_value = mock_res
        result: Dict = get_json(url)
        mock_get.assert_called_once_with(url)
        mock_res.json.assert_called_once()
        self.assertEqual(result, load)


if __name__ == '__main__':
    unittest.main()
