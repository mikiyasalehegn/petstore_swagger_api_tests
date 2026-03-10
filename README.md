# API Test Automation Framework (Python + Pytest)

![Python](https://img.shields.io/badge/python-3.x-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![API](https://img.shields.io/badge/API-testing-orange)

## 📖 Overview

This project is an **API test automation framework** built with **Python** and **pytest**.
It demonstrates how to structure automated API tests, validate responses, and organize reusable utilities for scalable test automation.

The framework uses the **Swagger Petstore API** to demonstrate testing of common API operations such as creating, retrieving, updating, and deleting resources.

The goal of this project is to practice:

* API testing
* Python automation
* Test framework architecture
* Clean and reusable test design

---

## 🚀 Tech Stack

* **Python**
* **Pytest**
* **Requests**
* **JSON / Schema Validation**
* **Git & GitHub**

---

## 📂 Project Structure

```
project-root
│
├── api/                    # API endpoint classes
│   ├── order_api.py
│   ├── pet_api.py
│   └── user_api.py
│
├── data/                   # Test data
│   └── test_data.py
│
├── tests/                  # Test cases
│   ├── test_pet.py
│   ├── test_pet_order.py
│   └── test_user.py
│
├── utils/                  # Helper utilities
│   ├── api_client.py
│   ├── assertions.py
│   ├── config.py
│   └── utility_functions.py
│
│
├── .gitignore
├──  conftest.py
├──  README.md
├── requirements.txt
```

---

## ⚙️ Setup

### 1️ Clone the repository

```bash
git clone https://github.com/mikiyasalehegn/petstore_swagger_api_tests.git

cd petstore_swagger_api_tests
```

### 2️ Create a virtual environment

```bash
python -m venv venv
```

### 3️ Activate the virtual environment

**Mac / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4 Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running Tests

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_pet.py
```

Run a specific test:

```bash
pytest tests/test_pet.py::test_create_pet
```

---

## 🧪 Example Test

Example test that validates an error response:

```python
def test_get_order_with_invalid_order_id(order_api):
    response = order_api.get_pet_order("invalid_id")
    assert_status_code(response, 404)
```

---

## 🔑 Key Features

* API client abstraction for reusable HTTP requests
* Clean separation between API logic and test logic
* Reusable assertion utilities
* Organized project structure
* Random test data generation
* Negative testing support

---

## 📚 Learning Objectives

This project demonstrates knowledge of:

* API testing principles
* pytest framework
* Python automation
* test architecture design
* reusable testing utilities
* Git version control

---

## 👨‍💻 Author

Mikiyas Mengistu

Python | API Testing | Test Automation

---

## 📌 Notes

This project was created for **learning and portfolio purposes** to demonstrate API automation testing skills.
