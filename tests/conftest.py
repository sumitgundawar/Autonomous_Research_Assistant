import pytest
from app.orchestration import Orchestrator
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

@pytest.fixture
def orchestrator():
    return Orchestrator()