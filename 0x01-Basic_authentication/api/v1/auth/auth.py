#!/usr/bin/env python3
"""
Contains the auth class
"""
from flask import request


class Auth:
    """
    The main class to manage the authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False
        """
        return Fasle

    def authorization_header(self, request=None) -> str:
        """
        returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None
        """
        return None
