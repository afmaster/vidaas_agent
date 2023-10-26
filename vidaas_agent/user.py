import requests
from typing import Any, Dict
import json


def user_discover(
        base_uri: str,
        client_id: str,
        client_secret: str,
        user_cpf_cnpj: str,
        val_cpf_cnpj: str
    ) -> Dict[str, Any]:
    """
    Makes a POST request to discover a user by CPF or CNPJ.

    Parameters:
    base_uri (str): The base URI of the API.
    client_id (str): The application's client ID.
    client_secret (str): The secret associated with the application.
    user_cpf_cnpj (str): 'CPF' for individual or 'CNPJ' for legal entity.
    val_cpf_cnpj (str): The value of the CPF or CNPJ.

    Returns:
    Dict[str, Any]: The response object returned by the API.

    Example:
        {
          "client_id": "4c9fb552-0387-4e5f-8727-6676fa88dce1",
          "client_secret": "Ny2n3hq67gQEFvH7",
          "user_cpf_cnpj": "CPF",
          "val_cpf_cnpj": "12345678901"
        }
    """

    headers = {
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "client_id": client_id,
        "client_secret": client_secret,
        "user_cpf_cnpj": user_cpf_cnpj,
        "val_cpf_cnpj": val_cpf_cnpj
    })

    endpoint = f"{base_uri}/v0/oauth/user-discovery"

    response = requests.request(
        "POST",
        endpoint,
        headers=headers,
        data=payload
    )

    return response.json()

