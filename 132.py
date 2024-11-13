import requests

username = "avielb"
# username = "talevi83"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)
if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        if "devops" in str(repo["full_name"]).lower():
            print(f"{username} - {repo["full_name"]}")
        print(repo["full_name"])

    # Save the repos data to a text file
    # repo_file = open('repo_file.txt', 'w')
    # repo_file.writelines(str(repos))
    # repo_file.close()