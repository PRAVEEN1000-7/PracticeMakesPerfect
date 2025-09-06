import requests

# simple mocking with custom db
database = {
    1 : "Ben",
    2 : "Gwen",
    3 : "Kevin"
}

def get_user_name_from_db(n):
    return database.get(n)

# mocking with api
def get_user_data(user_id):
    
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
    return {"error": "User not found"}

