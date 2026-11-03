"""Command-line interface for MCP Federation Router."""
import argparse
from .router import FederationRouter

def main():
    parser = argparse.ArgumentParser(description="MCP Federation Router CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate federated multi-server routing")
    args = parser.parse_args()

    router = FederationRouter()
    router.register_endpoint("git", "http://localhost:8001/mcp", ["clone", "commit", "push"])
    router.register_endpoint("db", "http://localhost:8002/mcp", ["query", "migrate"])

    ns, url = router.route("git_commit")
    print(f"Tool 'git_commit' routed to namespace '{ns}' at {url}")
    print("All federated tools:", router.list_tools())

if __name__ == "__main__":
    main()
