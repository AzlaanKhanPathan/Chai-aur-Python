import requests

def fetch_joke_id():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/100"
    response = requests.get(url)
    data = response.json()

    if data['success'] and "data" in data:
        user_data = data['data']["id"]
        return user_data
    else :
        raise Exception("Could not find joke")
    

def main():
    try:
        joke = fetch_joke_id()
        print(f"The Joke id is: ${joke}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
     main()