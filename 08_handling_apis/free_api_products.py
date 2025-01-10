import requests

def fetch_product():
    url = "https://api.freeapi.app/api/v1/public/randomproducts"
    response = requests.get(url)
    data = response.json()

    if data['success'] and "data" in data:
        user_data = data['data']["data"]
        for user in user_data:
            pr_1 = f"{user['title']}"
            return pr_1
        raise Exception("Failed to fetch the product")

def main():
    try:
        product = fetch_product()
        print(f"The Product is: {product}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()