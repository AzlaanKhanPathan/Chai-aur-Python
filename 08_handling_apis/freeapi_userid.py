import requests

def user_by_id():
    url = "https://api.freeapi.app/api/v1/public/randomusers/13"
    response = requests.get(url)
    data = response.json()
    if data['success'] and "data" in data:
        user_data = data['data']
        user_id = user_data['login']['uuid']
        return user_id
    else: 
        raise Exception("Could not find the user id")

def main():
    try:
        userid = user_by_id()
        print(f"Userid: {userid}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()