import requests
from typing import Any, Dict, List
import json


def register_application(
        url: str,
        name: str,
        comments: str,
        redirect_uri: List[str],
        email: str
    ) -> requests.Response:
    """
    Makes an API request and returns the response.

    Parameters:
    url (str): The URL of the API endpoint.
    name (str): The name parameter for the API request.
    comments (str): The comments parameter for the API request.
    redirect_uri (list): The redirect_uri parameter for the API request.
    email (str): The email parameter for the API request.
    data (dict, optional): The data to include in the body of the request (for POST, PUT, etc.). Defaults to None.

    The HTTP method used for the request is 'POST'.

    Returns:
    requests.Response: The response object returned by the API.

    Response Example:
        {
          "status": "success",
          "message": "New Client Application registered with Sucess",
          "client_id": "4c9fb552-0387-4e5f-8727-6676fa88dce1",
          "client_secret": "Ny2n3hq67gQEFvH7"
        }
    """

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = json.dumps({
        "name": name,
        "comments": comments,
        "redirect_uris": redirect_uri,
        "email": email
    })


    endpoint = f"{url}/v0/oauth/application"

    response = requests.request(
        "POST",
        url=endpoint,
        headers=headers,
        data=payload
    )

    return response.json()



def app_token(url: str, client_id: str, client_secret: str) -> Dict[str, Any]:
    """
    Request an application token from the API using client credentials.

    This function sends a POST request to the API to obtain an application token
    using the client credentials grant type.

    Parameters:
    url (str): The base URL of the API.
    client_id (str): The client ID for the application.
    client_secret (str): The client secret for the application.

    Returns:
    Dict[str, Any]: A dictionary containing the response data from the API.
                    Typically, this includes the access token and its details.
    """
    endpoint = f"{url}/v0/oauth/client_token"

    payload = f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url=endpoint, headers=headers, data=payload)

    return response.json()
