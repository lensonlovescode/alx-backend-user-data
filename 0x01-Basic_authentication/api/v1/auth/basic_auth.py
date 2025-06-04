#!/usr/bin/env python3
"""
Contains a class BasicAuth which inherits from the Auth class
"""
from .auth import Auth


class BasicAuth(Auth):
    """
    The basic authentication class that inherits from the auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the base64 authorization header
        """
        if authorization_header is None:
            return None

        arr = str(authorization_header).split(' ')
        if arr[0] != "Basic":
            return None

        return arr[1]
