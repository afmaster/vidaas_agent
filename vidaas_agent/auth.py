import requests
from typing import Any, Dict, Union
import json


def authorizations_qrcode(
        base_uri: str,
        client_id: str,
        code_challenge: str,
        scope: str = 'single_signature',
        login_hint: str = None,
        lifetime: int = None,
        redirect_uri: str = None
    ) -> str:

    """
    Constructs an HTTPS query for authorization and returns the URL.

    Parameters:
    base_uri (str): The base URI of the API.
    client_id (str): The application's client ID.
    code_challenge (str): The code challenge as per RFC 7636.
    scope (str, optional): The scope of the authorization request. Defaults to 'single_signature'. Alt: 'signature_session'.
    login_hint (str, optional): CPF or CNPJ value for certificate selection. Defaults to None.
    lifetime (int, optional): Desired lifetime of the token in seconds. Defaults to None.
    redirect_uri (str, optional): Redirect URI for notification. Defaults to None.

    Returns:
    str: The constructed HTTPS query URL.

    The access of this URL will initiate the authorization process via qr code to the client. Then a new url is
    generated by API and access point is used to redirect the client again to the platform.
    Exemple: <REDIRECT_URI>?code=2b15b0e1-bbf2-4e55-99b8-93cf824576b1&state=NONE
    """

    # Base query parameters
    query_params = {
        "client_id": client_id,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "response_type": "code",
        "scope": scope
    }

    # Optional query parameters
    if login_hint:
        query_params["login_hint"] = login_hint
    if lifetime:
        query_params["lifetime"] = str(lifetime)
    if redirect_uri:
        query_params["redirect_uri"] = redirect_uri

    # Constructing the HTTPS query URL
    query_string = "&".join(f"{key}={value}" for key, value in query_params.items())
    https_query_url = f"{base_uri}/v0/oauth/authorize?{query_string}"

    return https_query_url


def authentication(base_uri: str, authorization_code: str) -> Union[Dict, None]:
    """
        Makes an authentication request and returns the JSON response.

        Parameters:
        base_uri (str): The base URI of the API.
        authorization_code (str): The authorization code returned from the Authorization service, through
        the function `authorize_vidaas`


        Returns:
        dict or None: The JSON response as a dictionary, or None if the request fails.

        Example:
            {
                "authorizationToken":
                "eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..
                nYWhIcwNUH_22Upe1BSUTQ.
                oXT7UF2Mvtm5C6CjpdEGxcL_9XM86oNh4w0iGgUkQVGBla0CNnNW0_QbGx73Ldnu81kydOuz
                tSj3wfWUQf3t7IftvVMuyfdigW4_
                lz1LcC2q3p9N32iSEGb5VPzzSKqiZGa3asfMgEPjr3xYo7Lo3biTtbVPrChPLHslMi--
                b7DXXOIZ23N2R5bCT2_h6pj6PyBnXsEWl5uaF9v5PSXsQ.ZuLdlRZkfGBoqrxbj5tgTg",
                "redirectUrl": "push://<URI gerada no cadastro de aplicação>?
                code=8b1bde77-3647-4d76-1289-a2ec97c75a4d&state=NONE"
            }
    """

    # Constructing the URL
    url = f"{base_uri}/valid/api/v1/trusted-services/authentications?code={authorization_code}"

    # Making the GET request
    response = requests.get(url, headers={"Accept": "application/json"})

    # Checking for a successful response
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve authentication: {response.status_code}")
        return None



def get_token(base_uri: str, client_id: str, client_secret: str, authorization_code: str, code_verifier: str, redirect_uri: str) -> Dict[str, Any]:
    """
    Obtain an access token from the API using the authorization code flow.

    This function sends a POST request to the API to exchange an authorization code
    for an access token. It uses the authorization code flow with PKCE (Proof Key for Code Exchange).

    Parameters:
    base_uri (str): The base URL of the API.
    client_id (str): The client ID for the application.
    client_secret (str): The client secret for the application.
    authorization_code (str): The authorization code received from the authorization server.
    code_verifier (str): The code verifier used for PKCE.
    redirect_uri (str): The redirect URI registered with the application.

    Returns:
    Dict[str, Any]: A dictionary containing the response data from the API.
                    Typically, this includes the access token and its details.
    """
    url = f"{base_uri}/v0/oauth/token"

    payload = f'grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&code_verifier={code_verifier}&code={authorization_code}&redirect_uri={redirect_uri}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers, data=payload)

    return response.json()