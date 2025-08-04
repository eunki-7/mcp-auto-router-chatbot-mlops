"""
Router module for handling multi-component processing (MCP) routing logic.
This module decides which model/component to route user requests to,
based on the input text and pre-defined routing rules.
"""
from typing import Dict

class Router:
    def __init__(self):
        self.routing_rules = {
            "faq": "vector_search",
            "chat": "llm_chat"
        }

    def route(self, user_input: str) -> Dict[str, str]:
        if "FAQ" in user_input.upper():
            return {"component": self.routing_rules["faq"]}
        return {"component": self.routing_rules["chat"]}
