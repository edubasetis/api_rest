from fastapi.testclient import TestClient

from .eduAPI import app

client = TestClient(app)

# Cual es el objetivo de testear?
# Que se quiere testear?

# Run the test: pytest

def test_create_existing_item():
