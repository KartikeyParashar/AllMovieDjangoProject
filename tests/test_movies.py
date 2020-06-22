import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()


class TestCasesForMovie:

    def test_for_add_movie(self):
        ENDPOINT = 'movie/add/'
        url = os.getenv('BASE_URL') + ENDPOINT
        data = {
                "movie_name": "Baahubali: The Beginning",
                "release_date": "2015-07-10",
                "plot": "In the kingdom of Mahishmati, while pursuing his love, "
                        "Shivudu learns about the conflict ridden past of his family "
                        "and his legacy. He must now prepare himself to face his newfound arch-enemy.",
                "poster": "https://en.wikipedia.org/wiki/Baahubali:_The_Beginning#/media/File:"
                          "Baahubali_The_Beginning_Movie_Poster.jpg",
                "actor": [
                            "Prabhas", "Anushka Shetty"
                         ],
                "producer": [
                                "S. S. Rajamouli"
                            ]
                }
        headers = {'Content-Type': 'application/json'}
        response_ = requests.post(url, data=json.dumps(data), headers=headers)
        assert response_.status_code == 201

    def test_for_get_movie(self):
        ENDPOINT = 'movie/get/'
        url = os.getenv('BASE_URL') + ENDPOINT
        headers = {'Content-Type': 'application/json'}
        response_ = requests.get(url, headers=headers)
        assert response_.status_code == 200

    def test_for_get_movie_by_id(self):
        ENDPOINT = 'movie/get/1/'
        url = os.getenv('BASE_URL') + ENDPOINT
        headers = {'Content-Type': 'application/json'}
        response_ = requests.get(url, headers=headers)
        assert response_.status_code == 200