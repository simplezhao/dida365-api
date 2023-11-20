import requests
import os
import json
from loguru import logger


class TickTickClient:

    def __init__(self, url: str = None, *, phone: str = None, password: str = None):
        self._url = url or 'https://api.dida365.com'
        self.headers = {
            'User-Agent': 'TickTick/M-5010',
            'Content-Type': 'application/json;charset=UTF-8',
        }
        self._phone = phone
        self._password = password

    def get_token(self):
        """
        get ticktick token
        :return: token
        """
        url = self._url + '/api/v2/user/signon'
        resp = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps({
                'phone': self._phone,
                'password': self._password,
            })
        )
        return json.loads(resp.content.decode('utf8'))['token']

    def get_completed_tasks(self, start_time: str, end_time: str, limit: int = 100):
        """
        get completed tasks
        :param start_time: utc date, formate: %Y-%m-%d %H:%M:%S
        :param end_time: task end time, formate: %Y-%m-%d %H:%M:%S
        :param limit: default 100, max task = max(limit, you tasks)
        :return: tasks
        """
        url = self._url + '/api/v2/project/all/completed'
        self.headers.update({'Authorization': f"OAuth {self.get_token()}"})
        resp = requests.get(
            url=url,
            params={
                'from': start_time,
                'to': end_time,
                'limit': limit,
            },
            headers=self.headers,
        )
        if resp.status_code == 200:
            return json.loads(resp.content.decode('utf8'))

        else:
            logger.error(f"get completed task failed, status code: {resp.status_code}, "
                         f"content: {resp.content.decode('utf8')}")
            return None


