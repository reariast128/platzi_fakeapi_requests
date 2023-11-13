import api_handle

def run():
    response = api_handle.get_categories()
    print(response.text)
    print(response.status_code)

if __name__ == "__main__":
    run()