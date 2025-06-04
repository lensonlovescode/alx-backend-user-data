#!/usr/bin/env python3
"""
Contains a class BasicAuth which inherits from the Auth class
"""
from .auth import Auth
import base64


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

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        decodes the base 64 string into an ascii compaatible form
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encoded_str_to_bytes = base64_authorization_header.encode()
            encoded_bytes_to_base64 = base64.b64decode(encoded_str_to_bytes)
            decoded_str = encoded_bytes_to_base64.decode('utf-8')
            return decoded_str
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        Extracts and returns the user email and password
        from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        arr = decoded_base64_authorization_header.split(':')
        return (arr[0], arr[1])
