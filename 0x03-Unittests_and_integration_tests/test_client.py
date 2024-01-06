#!/usr/bin/env python3
""" unittest of client module functions """
import unittest
from typing import Dict, List, Mapping
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value: str = 'pla'
            test_class: GithubOrgClient = GithubOrgClient('pla')
            result: List = test_class.public_repos()
            mock_url.assert_called_once()
            self.assertEqual(result, ['a'])
        mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
            self, repo: Mapping, key: str, expected: bool) -> None:
        """ test has license method """
        test_class: GithubOrgClient = GithubOrgClient("google")
        result: bool = test_class.has_license(repo, key)
        self.assertEqual(result, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ integration test for whole class in client file """
    @classmethod
    def setUpClass(cls) -> None:
        """set up all requirements needed fot tests"""
        cls.get_patcher = patch('client.requests.get')
        cls.get_patcher.start()
        cls.mock_get = Mock(side_effect=cls.repos_payload)

    @classmethod
    def tearDownClass(cls) -> None:
        """ tear down all setups in first of test """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
