import argparse

from config import USERS_ENDPOINT
from using_requests import get_user

parser = argparse.ArgumentParser()
parser.add_argument("--use-httpx", action="store_true", help="If want to use httpx instead of requests")
args = parser.parse_args()

use_httpx = args.use_httpx

if __name__ == "__main__":
    if use_httpx:
        print("next")
    else:
        print(get_user(USERS_ENDPOINT, 2))
