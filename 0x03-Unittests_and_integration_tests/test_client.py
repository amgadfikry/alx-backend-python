#!/usr/bin/env python3
""" unittest of client module functions """
import unittest
from typing import Dict, List
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ class to test client functions
        inside class
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, name: str, mock_get: Mock) -> None:
        """ method that test org method in GithubOrgClient class """
        test_class: GithubOrgClient = GithubOrgClient(name)
        test_class.org()
        mock_get.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(name))

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_prop: PropertyMock):
        """ test method public repo url"""
        mock_prop.return_value = {'repos_url': 'pla'}
        call_class: GithubOrgClient = GithubOrgClient("pla")
        result: str = call_class._public_repos_url
        self.assertEqual(result, 'pla')

    @patch('client.get_json')
    def test_public_repos(self, mock_get: Mock) -> None:
        """ test public repos attribute"""
        mock_get.return_value: List = [{'name': 'a', 'license': None}]
        with patch('client.GithubOrgClient._public_repos_url') as mock_url:
            mock_url.return_value: str = 'pla'
            test_class: GithubOrgClient = GithubOrgClient('pla')
            result: List = test_class.public_repos()
            mock_get.assert_called_once_with(mock_url)
            self.assertEqual(result, ['a'])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
            self, repo: Dict[str, Dict], license: str, res: bool) -> None:
        """ test has license method """
        test_class = GithubOrgClient('pla')
        result = test_class.has_license(repo, license)
        self.assertEqual(result, res)


if __name__ == '__main__':
    unittest.main()
