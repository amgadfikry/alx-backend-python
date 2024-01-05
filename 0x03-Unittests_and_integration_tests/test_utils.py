#!/usr/bin/env python3
""" module to test utils file functions """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """ class of unittest to test memoize
        function of utlis module
    """
    def test_memoize(self):
        """ method test memoize function"""
        class TestClass:
            """ class to test memorization with mock"""
            def a_method(self) -> int:
                """ method that return number """
                return 42

            @memoize
            def a_property(self) -> int:
                """ method call function of a_method """
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_method:
            call_class: TestClass = TestClass()
            call_class.a_property()
            call_class.a_property()
        mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
