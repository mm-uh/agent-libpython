# coding: utf-8

"""
    Agent Platform

    This is a specification for openapi using  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: agentPlatform@grs.uh.cu
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import lib_agent
from lib_agent.api.default_api import DefaultApi  # noqa: E501
from lib_agent.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = lib_agent.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_agent(self):
        """Test case for get_agent

        """
        pass

    def test_get_agents_by_function(self):
        """Test case for get_agents_by_function

        """
        pass

    def test_get_agents_names(self):
        """Test case for get_agents_names

        """
        pass

    def test_get_peers(self):
        """Test case for get_peers

        """
        pass

    def test_get_similar_agent(self):
        """Test case for get_similar_agent

        """
        pass

    def test_register_agent(self):
        """Test case for register_agent

        """
        pass


if __name__ == '__main__':
    unittest.main()
