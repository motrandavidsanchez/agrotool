import json

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

JSON_CONTENT_TYPE = "application/json"
JSON_API_CONTENT_TYPE = "application/vnd.api+json"
JSON_API_ACCEPT_HEADER = "application/vnd.api+json"
CONTENT_TYPE_JSON = 'application/json'

User = get_user_model()


def create_user(username, first_name='Admin', last_name='Root', email=None, is_super=True):
    user, created = User.objects.get_or_create(
        username=username,
        email='{}@root.com'.format(username) if email is None else email,
        is_staff=True,
        is_active=True,
        is_superuser=is_super,
        defaults=dict(
            first_name=first_name,
            last_name=last_name,
            password='password'
        )
    )
    return user


def get_authenticated_client(user=None):
    client = APIClient()
    if user is not None:
        client.force_authenticate(user=user)
    return client


def get(url, params=None, user_logged=None):
    url += "?{}".format(params) if params else ''
    client = get_authenticated_client(user_logged)
    response = client.get(url)
    return response


def post(url, data=None, content_type=JSON_CONTENT_TYPE,  user_logged=None):
    url = url + '/' if not url.endswith('/') else url
    client = get_authenticated_client(user_logged)

    response = client.post(url, data=json.dumps(data), content_type=content_type)
    return response
