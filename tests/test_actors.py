import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()


class TestCasesForActor:

    def test_for_add_actor(self):
        ENDPOINT = 'actor/add/'
        url = os.getenv('BASE_URL') + ENDPOINT
        data = {
                "actor_name": "Rana Daggubati",
                "gender": "M",
                "dob": "1984-12-14",
                "bio": "Rana Daggubati is an Indian film actor, producer, visual effects co-ordinator,"
                       " and photographer who appears in Telugu, Tamil, and Hindi movies. "
                       "He made his acting debut with the Telugu movie Leader and went on to star in "
                       "several south Indian and Hindi movies. The actor is the recipient of the State "
                       "Nandi Award for Best Special Effects for the movie Sainikudu."
                }
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code == 201

    def test_for_get_actor(self):
        ENDPOINT = 'actor/get/'
        url = os.getenv('BASE_URL') + ENDPOINT
        headers = {'Content-Type': 'application/json'}
        response_ = requests.get(url, headers=headers)
        assert response_.status_code == 200

    def test_for_get_actor_by_id(self):
        ENDPOINT = 'actor/get/1/'
        url = os.getenv('BASE_URL') + ENDPOINT
        headers = {'Content-Type': 'application/json'}
        response_ = requests.get(url, headers=headers)
        assert response_.status_code == 200
