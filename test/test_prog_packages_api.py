# coding: utf-8

"""
    Snippets API

    Test description  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import interdbclient
from interdbclient.api.prog_packages_api import ProgPackagesApi  # noqa: E501
from interdbclient.rest import ApiException


class TestProgPackagesApi(unittest.TestCase):
    """ProgPackagesApi unit test stubs"""

    def setUp(self):
        self.api = interdbclient.api.prog_packages_api.ProgPackagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_prog_packages_create(self):
        """Test case for prog_packages_create

        """
        pass

    def test_prog_packages_delete(self):
        """Test case for prog_packages_delete

        """
        pass

    def test_prog_packages_list(self):
        """Test case for prog_packages_list

        """
        pass

    def test_prog_packages_partial_update(self):
        """Test case for prog_packages_partial_update

        """
        pass

    def test_prog_packages_read(self):
        """Test case for prog_packages_read

        """
        pass

    def test_prog_packages_update(self):
        """Test case for prog_packages_update

        """
        pass


if __name__ == '__main__':
    unittest.main()