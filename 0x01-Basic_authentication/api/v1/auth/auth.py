#!/usr/bin/env python3
"""
Contains the auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    The main class to manage the authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False
        """
        if path is None:
            return True
        if path[len(path) - 1] != "/":
            path += "/"
        if excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None, request will be the request object
        """
        return None
