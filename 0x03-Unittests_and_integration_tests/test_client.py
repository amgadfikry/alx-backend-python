#!/usr/bin/env python3
""" unittest of client module functions """
import unittest
from typing import Dict
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""
    @parameterized.expand([
        ('google', {'load': 'google'}),
        ('abc', {'load': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(self, name: str, load: Dict, mock_get: MagicMock) -> None:
        """Tests the `org` method."""
        mock_get.return_value = MagicMock(return_value=load)
        gh_org_client = GithubOrgClient(name)
        self.assertEqual(gh_org_client.org(), load)
        mock_get.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(name)
        )


if __name__ == '__main__':
    unittest.main()
