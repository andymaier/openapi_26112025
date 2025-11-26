# coding: utf-8

from fastapi.testclient import TestClient


from typing import List, Optional  # noqa: F401
from openapi_server.models.article import Article  # noqa: F401


def test_articles_get(client: TestClient):
    """Test case for articles_get

    Get all Artikels
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/articles",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_articles_post(client: TestClient):
    """Test case for articles_post

    create an article
    """
    article = {"price":0.99,"name":"Cherry","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/articles",
    #    headers=headers,
    #    json=article,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

