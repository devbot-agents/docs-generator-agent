import pytest
from fastapi.testclient import TestClient
from jsonschema import validate
from main import app  # Ajuste este import de acordo com a estrutura do seu projeto

client = TestClient(app)

@pytest.fixture
def example_agent_data():
    return {
        "name": "Example Agent",
        "description": "This is a test agent for generating docs",
        "input_schema": "{}",
        "output_schema": "{}",
        "endpoint_url": "http://example.com/api"
    }

@pytest.fixture
def expected_output_schema():
    return {
        "type": "object",
        "properties": {
            "readme": {"type": "string"},
            "swagger": {"type": "string"},
            "examples": {"type": "string"},
            "agent_json": {"type": "string"}
        }
    }

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}

def test_execute_endpoint(example_agent_data, expected_output_schema):
    response = client.post("/api/v1/execute", json=example_agent_data)
    assert response.status_code == 200
    output_data = response.json()
    validate(instance=output_data, schema=expected_output_schema)

    # Verifica se todas as chaves esperadas estão presentes na resposta
    for key in expected_output_schema["properties"].keys():
        assert key in output_data
