
import requests


def call_api(url: str):
    try:
        response = requests.get(url)
        print(response.json())
    except Exception as err:
        print()



if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    call_api(url)
