"""Unit tests for FederationRouter."""
import unittest
from mcp_federation_router.router import FederationRouter

class TestFederationRouter(unittest.TestCase):
    def setUp(self):
        self.router = FederationRouter()
        self.router.register_endpoint("db", "http://db-mcp", ["query", "execute"])

    def test_routing(self):
        ns, url = self.router.route("db_query")
        self.assertEqual(ns, "db")
        self.assertEqual(url, "http://db-mcp")

    def test_unregistered_tool(self):
        with self.assertRaises(KeyError):
            self.router.route("unknown_tool")

    def test_list_tools(self):
        tools = self.router.list_tools()
        self.assertIn("db_query", tools)
        self.assertIn("db_execute", tools)

if __name__ == "__main__":
    unittest.main()
