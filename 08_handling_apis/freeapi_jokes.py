import requests

def fetch_product_id():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%252Cid%252Ccontent&page=1"
    response = requests.get(url)
    data = response.json()

    if data['success'] and "data" in data:
        user_data = data['data']["data"]
        for user in user_data:
            joke_1 = {user['content']}
        return joke_1
    else :
        raise Exception("Could not find joke")
    

def main():
    try:
        joke = fetch_product_id()
        print(f"The Joke is: ${joke}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
     main()