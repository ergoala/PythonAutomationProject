import pytest
import sys

if __name__ == "__main__":
    sys.exit(pytest.main([
        "-v",
        "--tb=short",
        "tests/test_bdd_e2e.py::test_e2e_happy_path"
    ]))
