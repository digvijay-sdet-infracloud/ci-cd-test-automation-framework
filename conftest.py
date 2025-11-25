import json
import os
import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action="store", 
        default="dev",
        help="Environment to run tests against (dev, staging, prod)"
    )

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    file_path = f"tests/config/{env}_config.json"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file for environment '{env}' not found at {file_path}")

    with open(file_path) as f:
        return json.load(f)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser, config):
    context = browser.new_context(base_url=config["base_url"])
    yield context
    context.close()

    
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def credentials(config):
    return {
        "username": config["username"],
        "password": config["password"]
    }
