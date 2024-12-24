import pytest
import requests
from Config.config import UserData



 # Replace with your actual API token

@pytest.fixture(scope="module")
def api_client():
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {UserData.API_TOKEN}",
        "Content-Type": "application/json"
    })
    session.base_url = UserData.Base_url
    return session
