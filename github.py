import requests

def main():
    user_name = str(input("Enter github username:\t"))
    url = f"https://api.github.com/users/{user_name}/events"
    output = requests.get(url)
    if output.status_code == 200:
        response_wrap = output.json()
    for response in response_wrap:
        format = f"- Repo:{response['repo']['url']}\n- Event:{response['type']}\n- Actor {response['actor']['login']}\n-   Created at {response['created_at']}\n"
        print(format)

main()
