![Selenium E2E Tests](https://github.com/Himans-03/selenium-e2e-framework/actions/workflows/ci.yml/badge.svg)
# 🧪 Selenium E2E Test Framework

![CI](https://github.com/Himans-03/selenium-e2e-framework/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.20-green)
![pytest](https://img.shields.io/badge/pytest-8.2-orange)

A professional, beginner-friendly **End-to-End test automation framework** built with:

- 🐍 **Python** + **pytest** — clean, readable tests
- 🌐 **Selenium WebDriver** — real browser automation
- 🏗️ **Page Object Model (POM)** — maintainable, DRY structure
- 🤖 **GitHub Actions CI/CD** — tests run automatically on every push

> **Target site:** [SauceDemo](https://www.saucedemo.com) — a purpose-built e-commerce demo site designed for Selenium practice.

---

## 📁 Project Structure

```
selenium-e2e-framework/
│
├── .github/
│   └── workflows/
│       └── ci.yml              ← GitHub Actions pipeline
│
├── config/
│   └── config.py               ← URLs, credentials, timeouts
│
├── pages/                      ← Page Object Model classes
│   ├── base_page.py            ← Shared Selenium helpers
│   ├── login_page.py           ← Login page actions & locators
│   └── products_page.py        ← Products page actions & locators
│
├── tests/
│   ├── conftest.py             ← pytest fixtures (browser setup/teardown)
│   ├── test_login.py           ← Login test cases
│   └── test_products.py        ← Products page test cases
│
├── utils/
│   └── driver_factory.py       ← Creates the browser driver
│
├── reports/                    ← Auto-generated HTML test report
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Himans-03/selenium-e2e-framework.git
cd selenium-e2e-framework
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run all tests
```bash
pytest
```

### 5. View the HTML report
Open `reports/report.html` in your browser after tests finish.

---

## 🤖 CI/CD with GitHub Actions

Every push to `main` or `develop` automatically:
1. Spins up an Ubuntu machine
2. Installs Python and Chrome
3. Runs all tests in headless mode
4. Uploads an HTML report as a downloadable artifact

You can also trigger a run manually from the **Actions** tab on GitHub.

---

## ✅ Test Cases

| File | Test | Description |
|------|------|-------------|
| `test_login.py` | `test_successful_login` | Valid user lands on Products page |
| `test_login.py` | `test_locked_out_user_sees_error` | Locked account shows error message |
| `test_login.py` | `test_wrong_password_shows_error` | Wrong password shows error |
| `test_login.py` | `test_empty_username_shows_error` | Missing username shows validation |
| `test_login.py` | `test_empty_password_shows_error` | Missing password shows validation |
| `test_login.py` | `test_login_page_title` | Page title is correct |
| `test_products.py` | `test_products_page_title` | Title reads "Products" after login |
| `test_products.py` | `test_six_products_are_displayed` | Grid shows exactly 6 products |
| `test_products.py` | `test_add_to_cart_updates_badge` | Cart badge increments to 1 |
| `test_products.py` | `test_logout_redirects_to_login` | Logout returns to login page |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Selenium 4 | Browser automation |
| pytest | Test runner & assertions |
| webdriver-manager | Auto-installs ChromeDriver |
| pytest-html | Generates HTML test reports |
| GitHub Actions | Free CI/CD pipeline |

---

## 📖 Key Concepts Demonstrated

- **Page Object Model** — Each page has its own class. Tests never call Selenium directly.
- **Fixtures** — `conftest.py` handles browser setup and teardown cleanly.
- **Headless testing** — Runs in CI without a display screen.
- **Automatic screenshots** — Saved to `reports/` on test failure.

---

## 🙋 Author

**Himanshu Shekhar** — [LinkedIn](https://linkedin.com) · [GitHub](https://github.com)
