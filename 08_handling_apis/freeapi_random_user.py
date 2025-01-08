import requests

def get_random_users():
    # Handling the dictionary
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    data = response.json()
    if data['success'] and "data" in data:
        user_data = data['data']
        username = user_data['login']['username']
        location = user_data["location"]["country"]
        return username , location
    else:
        raise Exception("Failed to fetch user data")


def main():
    try :
        randomuser , randomcountry = get_random_users()
        print(f"Username: {randomuser} \nCountry: {randomcountry}")
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
