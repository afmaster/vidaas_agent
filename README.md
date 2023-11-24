

# Vidaas Agent

## Introduction

Vidaas Agent is a Python library designed to simplify interactions with the VIDaaS (Valid Certificadora) API. This library provides a set of convenient functions to handle various aspects of digital signature processes, including authentication, user discovery, authorization, and signing documents.

## Features

- Easy registration and authentication with the VIDaaS API.
- Discover if a client is registered in VIDaaS.
- Handle authorization processes and generate QR codes for signature sessions.
- Sign PDF documents digitally using VIDaaS.

## Installation

You can install VidaasAgent using pip:

```bash
pip install git+https://github.com/afmaster/vidaas_agent.git
```
## Use
URIs for Valid PSC.

Production: https://certificado.vidaas.com.br

This is the only one recommended. Including for tests.

Whe have added a function in utils/encryption for code_challenge and code_verifier, as outlined in RFC 7636 and required in the VIDaaS authentication proccess.


## API Documentation 
Link to the full API documentation for users who want more detailed information:

[VALID API DOCUMENTATION](https://valid-sa.atlassian.net/wiki/spaces/PDD/pages/958365697/Manual+de+Integra+o+com+VIDaaS+-+Certificado+em+Nuvem)

## License
This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE).

## Contact

Contact-me: andre@franciscatto.com
