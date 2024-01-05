#!/usr/bin/env python3
""" unittest of client module functions """
import unittest
from typing import Dict
from unittest.mock import patch, Mock, MagicMock
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
            self, name: str, load: Dict, mock_get: MagicMock) -> None:
        """ method that test org method in GithubOrgClient class """
        mock_get.return_value = MagicMock(return_value=load)
        call_class: GithubOrgClient = GithubOrgClient(name)
        self.assertEqual(call_class.org(), load)
        mock_get.assert_called_once_with(call_class.ORG_URL.format(org=name))


if __name__ == '__main__':
    unittest.main()
