"""Multi-server MCP routing and namespace dispatch."""
from typing import Dict, List, Any, Optional, Tuple


class FederationRouter:
    def __init__(self):
        self._endpoints: Dict[str, Dict[str, Any]] = {}
        self._tool_to_endpoint: Dict[str, str] = {}

    def register_endpoint(self, namespace: str, endpoint_url: str, tools: List[str]) -> None:
        self._endpoints[namespace] = {
            "url": endpoint_url,
            "tools": tools
        }
        for t in tools:
            # Map namespaced and bare tool
            self._tool_to_endpoint[f"{namespace}_{t}"] = namespace
            if t not in self._tool_to_endpoint:
                self._tool_to_endpoint[t] = namespace

    def route(self, tool_name: str) -> Tuple[str, str]:
        """Returns (namespace, endpoint_url) for a tool."""
        if tool_name in self._tool_to_endpoint:
            ns = self._tool_to_endpoint[tool_name]
            return ns, self._endpoints[ns]["url"]
        raise KeyError(f"Tool '{tool_name}' not registered in any federated endpoint.")

    def list_tools(self, namespace: Optional[str] = None) -> List[str]:
        if namespace:
            return self._endpoints.get(namespace, {}).get("tools", [])
        all_tools = []
        for ns, ep in self._endpoints.items():
            for t in ep["tools"]:
                all_tools.append(f"{ns}_{t}")
        return all_tools
