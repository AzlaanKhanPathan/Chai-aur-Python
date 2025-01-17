import requests

def fetch_random_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data['success'] and "data" in data:
        user_data = data['data']["content"]
        return user_data
    else :
        raise Exception("Could not find joke")
    

def main():
    try:
        joke = fetch_random_joke()
        print(f"The Joke is: ${joke}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
     main()