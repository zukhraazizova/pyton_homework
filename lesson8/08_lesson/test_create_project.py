from api_projects import ProjectAPI

def test_positive_create_project():
    response = ProjectAPI.create_project("MyProject")
    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    project_id = data["id"]

    project_response = ProjectAPI.get_project(project_id)
    assert project_response.status_code == 200
    assert project_response.json()["title"] == "MyProject"

# Негативный тест
def test_negative_create_project_empty_name():
    response = ProjectAPI.create_project("")
    assert response.status_code == 400