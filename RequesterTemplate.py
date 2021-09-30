import json
from uuid import UUID

import requests

from errors.RequestError import RequestError


class RequesterTemplate:
    def __init__(self, headers, url):
        self.headers = headers
        self.url = url

    def _get_request(self, url_extension):
        r = requests.get(self.url + url_extension, headers=self.headers)
        json_text = json.loads(r.text)
        if not json_text["success"]:
            raise RequestError(f'{json_text["error"]}: {json_text["message"]}')

        return json_text

    def _post_request(self, url_extension, data=None, json=None):
        r = requests.post(self.url + url_extension, headers=self.headers, data=data, json=json)
        json_text = json.loads(r.text)
        if not json_text["success"]:
            raise RequestError(f'{json_text["error"]}: {json_text["message"]}')
        return json_text

    def _delete_request(self, url_extension, data=None):
        r = requests.delete(self.url + url_extension, headers=self.headers, data=data)
        json_text = json.loads(r.text)
        if not json_text["success"]:
            raise RequestError(f'{json_text["error"]}: {json_text["message"]}')
        return json_text