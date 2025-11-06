from api_projects import ProjectAPI

def test_positive_update_project(create_test_project):
    response = ProjectAPI.update_project(create_test_project, "UpdatedProject")
    assert response.status_code == 200

    # Проверка через GET
    project = ProjectAPI.get_project(create_test_project)
    assert project.json()["title"] == "UpdatedProject"

def test_negative_update_project_invalid_id():
    response = ProjectAPI.update_project("999999", "NewTitle")
    assert response.status_code == 404