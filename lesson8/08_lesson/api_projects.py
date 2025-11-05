import requests

BASE_URL = "https://ru.yougile.com"
TOKEN = "PpFz2FSBtVC9eOm7Cjy8sgORmfUz-D31tfDpNMINNLja+MIYUj8o45xQiYWdh7CS"

class ProjectAPI:
    @staticmethod
    def get_headers():
        return {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }

    @staticmethod
    def create_project(title: str):
        payload = {"title": title}
        response = requests.post(
            f"{BASE_URL}/api-v2/projects",
            json=payload,
            headers=ProjectAPI.get_headers()
        )
        print(response.status_code, response.text)  # Для отладки
        return response

    @staticmethod
    def get_project(project_id: str):
        response = requests.get(
            f"{BASE_URL}/api-v2/projects/{project_id}",
            headers=ProjectAPI.get_headers()
        )
        print(response.status_code, response.text)  # Для отладки
        return response

    @staticmethod
    def update_project(project_id: str, title: str):
        payload = {"title": title}  
        response = requests.put(
            f"{BASE_URL}/api-v2/projects/{project_id}",
            json=payload,
            headers=ProjectAPI.get_headers()
        )
        print(response.status_code, response.text)  # Для отладки
        return response