import uuid
import logging
import hashlib
from typing import Optional
from urllib.parse import urlencode

import jwt

from upbit import access_key, secret_key


def authorize_token(query: Optional[dict] = None) -> str:
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    if query:
        normal_q = {}
        list_q = {}
        for k, v in query.items():
            if isinstance(v, list):
                list_q[k] = v
            else:
                normal_q[k] = v
        query_string = urlencode(normal_q)
        for k, l in list_q.items():
            query_string += '&'
            query_string += '&'.join([f'{k}={item}' for item in l])
        logging.info(query_string)

        sha512 = hashlib.sha512()
        sha512.update(query_string.encode())
        query_hash = sha512.hexdigest()
        payload.update({
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        })
        logging.info(payload)

    jwt_token = jwt.encode(payload, secret_key)
    authorization_token = f'Bearer {jwt_token}'
    return authorization_token
