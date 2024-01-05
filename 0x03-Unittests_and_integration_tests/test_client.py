#!/usr/bin/env python3
""" unittest of client module functions """
import unittest
from typing import List
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ class to test client functions """
    @parameterized.expand([
        ('google', {'load': 'google'}),
        ('abc', {'load': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(
            self, name: str, load: str, mock_get: Mock) -> None:
        """ method that test org method in GithubOrgClient class """
        mock_res: Mock = Mock()
        mock_res.json.return_value = load
        mock_get.return_value = mock_res
        call_class: GithubOrgClient = GithubOrgClient(name)
        result: Mock = call_class.org()
        mock_get.assert_called_once_with(call_class.ORG_URL.format(org=name))

if __name__ == '__main__':
    unittest.main()
