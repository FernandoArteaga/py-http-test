import requests


def get_user(url: str, _id: int) -> dict | None:
    response = requests.get(f"{url}/{_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None
