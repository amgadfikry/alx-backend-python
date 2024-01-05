#!/usr/bin/env python3
""" unittest of client module functions """
import unittest
from typing import Dict
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ class to test client functions
        inside class
    """
    @parameterized.expand([
        ('google', {'load': 'google'}),
        ('abc', {'load': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(
            self, name: str, load: Dict, mock_get: Mock) -> None:
        """ method that test org method in GithubOrgClient class """
        mock_res: Mock = Mock()
        mock_res.return_value = load
        mock_get.return_value = mock_res
        call_class: GithubOrgClient = GithubOrgClient(name)
        result: Dict = call_class.org()
        mock_get.assert_called_once_with(call_class.ORG_URL.format(org=name))
        mock_res.assert_called_once()
        self.assertEqual(result, load)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_prop: PropertyMock):
        """ test method public repo url"""
        mock_prop.return_value = {'repos_url': 'pla'}
        call_class: GithubOrgClient = GithubOrgClient("pla")
        result: str = call_class._public_repos_url
        self.assertEqual(result, 'pla')


if __name__ == '__main__':
    unittest.main()
