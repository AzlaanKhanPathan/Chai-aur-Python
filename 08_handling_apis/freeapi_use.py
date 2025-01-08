import requests

def fetch_random_user_freeapi():
    url = 'https://api.freeapi.app/api/v1/public/randomusers'
    response = requests.get(url)
    data = response.json()
    if data['success'] and "data" in data:
        user_data = data['data']["data"]
        for user in user_data:
            username = f"{user['login']['username']}"
            location = f"{user['location']['country']}"
            return username , location
        raise Exception("Failed to fetch user data")
    

def main():
    try :
        username, country = fetch_random_user_freeapi()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()

