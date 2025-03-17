import requests
import base64

class GitHubService:
    def __init__(self, username: str, token: str = None):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"

    def get_repo_readme(self, repo_name: str):
        url = f"{self.base_url}/repos/{self.username}/{repo_name}/readme"
        headers = {"Accept": "application/vnd.github.v3+json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Ошибка при загрузке README: {response.status_code}")

        readme_data = response.json()
        readme_content = base64.b64decode(readme_data["content"]).decode("utf-8")
        return readme_content

    def get_user_repos(self):
        url = f"{self.base_url}/users/{self.username}/repos"
        headers = {"Accept": "application/vnd.github.v3+json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Ошибка при загрузке репозиториев: {response.status_code}")

        repos = response.json()
        return [
            {
                "name": repo["name"],
                "description": repo["description"],
                "html_url": repo["html_url"],
                "stargazers_count": repo["stargazers_count"],
            }
            for repo in repos
            if not repo["fork"] and repo["name"] != self.username  # Исключаем форки и репозиторий профиля
        ]