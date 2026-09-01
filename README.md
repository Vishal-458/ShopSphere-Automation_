# ShopSphere Automation

A QA automation framework built using Python, Playwright, Pytest, API testing, SQL database testing, logging, failure screenshots, traces, parallel execution, and CI/CD.

## Tech Stack

- Python
- Playwright
- Pytest
- Requests
- SQLite
- SQL
- Pytest-xdist
- GitHub Actions

## Project Structure

```text
ShopSphere-Automation/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── config/
│   └── qa.json
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── test_data/
│   └── test_data.json
│
├── tests/
│   ├── test_first.py
│   ├── test_login.py
│   ├── test_home.py
│   ├── test_product.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_api.py
│   ├── test_api_ui.py
│   └── test_database.py
│
├── utils/
│   ├── config_reader.py
│   ├── test_data_reader.py
│   ├── api_client.py
│   ├── db_helper.py
│   └── logger.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md  



# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

# Run all tests
pytest -v

# Run Chromium
pytest -v --browser chromium

# Run Firefox
pytest -v --browser firefox

# Run WebKit
pytest -v --browser webkit

# Run staging
pytest -v --env staging

# Run smoke tests
pytest -v -m smoke

# Run API tests
pytest -v -m api

# Run database tests
pytest -v -m database

# Run in parallel
pytest -v -n auto

# Run with retry
pytest -v --reruns 1

# Generate HTML report
pytest -v --html=reports/report.html --self-contained-html