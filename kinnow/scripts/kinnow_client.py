import requests
from typing import Optional
from datetime import datetime
from uuid import UUID


def post_user_data(
    username: str,
    first_name: str,
    last_name: str,
    email: str,
    password: str,
):

    url = "http://localhost:8000/api/system_user/"

    data = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
    }

    response = requests.post(url, json=data)
    print(response.text)
    if response.status_code == 200:
        print("Data successfully posted.")
    else:
        print("Error posting data.")


post_user_data(
    username="john.doe1",
    first_name="John",
    last_name="Doe",
    email="john.doe@example.com",
    password="Test@1234",
)
