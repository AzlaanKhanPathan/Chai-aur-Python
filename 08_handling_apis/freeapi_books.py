import requests

def fetch_book():
    url = 'https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%252Cid%252Cetag%252CvolumeInfo&query=tech'
    response = requests.get(url)
    data = response.json()
    arr = data['data']['data']
    for d in range(len(arr)):
        print(d,arr[d]["volumeInfo"]['title'])
        # This line explains that if subtitle is not there , it is "None" data type 
        if arr[d]['volumeInfo'].get('subtitle'):
            print(d,arr[d]["volumeInfo"]['subtitle'])
        else:
            print("No subtitle available")

    ##### Wrong Method #######
    # print(type(data[data]))
    # if data['success'] and "data" in data:
    #     user_data = data['data']["data"]
    #     for user in user_data:
    #         title = f"{user['volumeInfo']}"
    #         return title
    #     raise Exception("Failed to fetch user data")
    

def extract_title():
    try :
        fetch_book()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    extract_title()

