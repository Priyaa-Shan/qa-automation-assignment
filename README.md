# QA Automation Assignment – Playwright + Python

## Overview

This project is a UI automation framework built using **Playwright with Python and pytest**.
It demonstrates:
- Page Object Model (POM)
- UI automation using Playwright
- Stable and deterministic test design
- Basic assertions and search validation scenario

---

## Tools Used
- Python 3
- Playwright
- pytest

### Why these tools?
- **Playwright**: Modern automation tool with auto-waiting and stable browser control
- **pytest**: Simple and powerful test framework for structuring tests
- **POM (Page Object Model)**: Improves maintainability and readability of test code

---

## Project Structure
qa-automation-assignment/
│
├── pages/
│ └── restaurant_page.py
│
├── tests/
│ ├── test_home_page.py
│ └── test_restaurant_search.py
│
├── test_data/
│ └── restaurants.html
│
├── reports/
│ └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md



---

## Test Scenarios
###  Part 1: Basic Assertions

- Navigate to a public website
- Assert page title
- Assert at least 2 visible UI elements

---

###  Part 2: Restaurant Search Scenario

Since real restaurant websites (like Yelp or Google Maps) contain:
- CAPTCHA protection
- dynamic DOM structures
- unstable selectors

A **controlled static dataset approach** was used instead.

Steps:
- Navigate to a local HTML page containing restaurant data
- Validate restaurant list is displayed
- Assert that at least one restaurant item exists

---

## Assumptions & Limitations
- Real-world restaurant platforms were avoided due to:
  - Bot detection (CAPTCHA)
  - Dynamic rendering issues
  - Unstable automation behavior

- A static HTML dataset was used to ensure:
  - Stable and repeatable test execution
  - No external dependency
  - CI/CD compatibility

---

## How to Run
### Install dependencies
```bash
pip install -r requirements.txt


### Install Playwright browsers
python -m playwright install

## Run tests
python -m pytest

## Generate HTML report
python -m pytest --html=reports/report.html --self-contained-html

