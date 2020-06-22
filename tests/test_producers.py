import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()


class TestCasesForProducer:

    def test_for_add_producer(self):
        ENDPOINT = 'producer/add/'
        url = os.getenv('BASE_URL') + ENDPOINT
        data = {
                "producer_name": "S. S. Rajamouli",
                "gender": "M",
                "dob": "1973-10-10",
                "bio": "Known for directing the historical fiction movies Baahubali: "
                       "The Beginning and Baahubali 2: The Conclusion, S. S. Rajamouli, "
                       "born Koduri Srisaila Sri Rajamouli, is an Indian film director "
                       "and screenwriter. He gained prominence in Telugu cinema with "
                       "blockbuster movies like Magadheera (2009), Eega (2012) and "
                       "Baahubali: The Beginning (2015). His other notable directorial "
                       "ventures are the sports drama film Sye, the social problem film "
                       "Vikramarkudu, drama films Maryada Ramanna and Chhatrapati. "
                       "Most of his movies are either dubbed or remade in various Indian "
                       "languages with successful reviews."
                }
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code == 201

    def test_for_get_producer(self):
        ENDPOINT = 'producer/get/'
        url = os.getenv('BASE_URL') + ENDPOINT
        headers = {'Content-Type': 'application/json'}
        response_ = requests.get(url, headers=headers)
        assert response_.status_code == 200

    def test_for_get_producer_by_id(self):
        ENDPOINT = 'producer/get/1/'
        url = os.getenv('BASE_URL') + ENDPOINT
        headers = {'Content-Type': 'application/json'}
        response_ = requests.get(url, headers=headers)
        assert response_.status_code == 200
