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