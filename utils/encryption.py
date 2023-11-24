import base64
import hashlib
import os

def RFC_7636_code_pair() -> tuple:
    """
        Generate a code verifier and a code challenge as per RFC 7636.

        The code verifier is a high-entropy cryptographic random string.
        The code challenge is derived from the code verifier using the SHA256 hash function,
        and is used in the authorization request.

        Main use is for deal with VIDaaS API.

        Returns:
            tuple: A tuple containing the code verifier and code challenge.
    """
    code_verifier = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8').replace('=', '')
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).decode('utf-8').replace('=', '')
    return code_verifier, code_challenge
