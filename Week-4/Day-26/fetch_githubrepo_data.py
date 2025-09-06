import requests

url = "https://api.github.com/users/octocat/repos"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    repos = response.json()
    
    print("Public Repositories of Octcat:")
    for repo in repos:
        print("•",repo['name'])
    
except requests.exceptions.HTTPError as e:
    print("HTTP Error:",e)
except requests.exceptions.ConnectionError as e:
    print("Connection Error:",e)
except requests.exceptions.Timeout:
    print("Request Timed Out")
except requests.exceptions.RequestException as e:
    print("Other Error:",e)