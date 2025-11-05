from api_projects import ProjectAPI


def test_positive_get_project(create_test_project):
    response = ProjectAPI.get_project(create_test_project)
    assert response.status_code == 200
    assert response.json()["id"] == create_test_project

#негативный тест

def test_negative_get_project_not_found():
    response = ProjectAPI.get_project(999999)
    assert response.status_code == 404