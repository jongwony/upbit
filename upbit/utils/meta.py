import requests
from inspect import signature

from upbit import server_api
from ..api.auth import authorize_token


def upbit_qs(func):
    sig = signature(func)

    def wrapper(*args, **kwargs):
        query = {}

        bound_args = sig.bind(*args, **kwargs)
        for k, v in bound_args.arguments.items():
            if isinstance(sig.parameters[k].annotation, list):
                query[f'{k}[]'] = v
            else:
                query[k] = v

        api_spec = func(*bound_args.args, **bound_args.kwargs)

        response = requests.request(
            method=api_spec['method'],
            url=server_api(api_spec['path']),
            params=query,
            headers={'Authorization': authorize_token(query)},
        )
        return response.json()

    return wrapper
