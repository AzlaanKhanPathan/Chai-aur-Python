import requests

def fetch_product_id():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/30"
    response = requests.get(url)
    data = response.json()

    if data['success'] and "data" in data:
        user_data = data['data']['id']
        # product_id = user_data['id']
        return user_data
    else :
        raise Exception("Could not find product id")
    

def main():
    try:
        id = fetch_product_id()
        print(f"The Product id is: ${id}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
     main()