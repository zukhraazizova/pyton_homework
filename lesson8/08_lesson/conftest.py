import pytest
from api_projects import ProjectAPI


@pytest.fixture
def create_test_project():
    response = ProjectAPI.create_project("AutoProject")
    assert response.status_code == 201
    project_id = response.json()["id"]
    return project_id