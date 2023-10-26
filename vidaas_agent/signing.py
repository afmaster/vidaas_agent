import requests
from typing import Dict, Union
import json


def sign(
        base_uri: str,
        access_token: str,
        hash_id: str,
        hash_alias: str,
        hash_value: str,
        hash_algorithm: str,
        base64_content: str,
        pdf_signature_page: str = 'true',
        signature_format: str = 'CAdES_AD_RB'
    ) -> Union[Dict, None]:
    """
    Makes a signature request and returns the JSON response.

    Parameters:
    base_uri (str): The base URI of the API.
    access_token (str): The access token for authorization.
    hash_id (str): Identifier of the content to be signed.
    hash_alias (str): Human-readable form of the content identifier.
    hash_value (str): Content to be signed.
    hash_algorithm (str): Object Identifier (OID) of the hash algorithm.
    base64_content (str): The base64 content of the PDF to be signed.
    certificate_alias (str, optional): Identifier of the certificate corresponding to the signing key. Defaults to None.
    padding_method (str, optional): Padding method for the signature. Defaults to None.
    pdf_signature_page (str, optional): Whether to add a signature page to the PDF. Defaults to 'true'.
    signature_format (str): format used to sign the document. Defaluts to CAdES_AD_RB. Also suported CMS

    Returns:
    dict or None: The JSON response as a dictionary, or None if the request fails.
    """
    url = f"{base_uri}/valid/api/v1/trusted-services/signatures"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        "hashes": [
            {
                "id": hash_id,
                "alias": hash_alias,
                "hash": hash_value,
                "hash_algorithm": hash_algorithm,
                "signature_format": signature_format,
                pdf_signature_page: pdf_signature_page,
                "base64_content": base64_content  # Assumindo que base64_content já está em formato string
            }
        ]
    })

    response = requests.post(url, headers=headers, data=payload)

    return response.json()
