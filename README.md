# API Data Analyzer

A beginner-friendly Python project that fetches data from a REST API and analyzes it using Python lists, dictionaries, loops, and functions.

Built as part of my **AI Engineer Journey — Week 4, Day 3**.

## Features

- Fetch posts from the JSONPlaceholder API.
- Display the total number of posts.
- Count posts belonging to each user.
- Filter posts by user ID.
- Search post titles using a keyword.
- Handle API request errors and invalid user input.
- Interactive, menu-driven command-line interface.

## Tech Stack

- **Language:** Python
- **HTTP Library:** Requests
- **API:** JSONPlaceholder
- **Concepts:** REST APIs, JSON, lists, dictionaries, functions, loops, list comprehensions, exception handling

## Project Structure

```text
api-data-analyzer/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Requirements

- Python 3.10 or later
- pip
- Internet connection

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sadique31/api-data-analyzer.git
cd api-data-analyzer
```

### 2. Create a virtual environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the project

**macOS / Linux:**

```bash
python3 main.py
```

**Windows:**

```bash
python main.py
```

## Data Source

This project uses the free [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts), which provides sample data for testing and learning.

The posts are demonstration data, not real social media content.

## Learning Outcomes

Through this project, I practised:

- Sending HTTP GET requests using Python.
- Converting API responses into Python data structures.
- Filtering and searching records.
- Counting records using dictionaries.
- Validating user input.
- Handling request errors.
- Organizing code into reusable functions.

## Future Improvements

- Add search by post body.
- Handle invalid JSON responses separately.
- Add unit tests.
- Export analysis results to CSV or JSON.
- Add data visualization.

## Author

**Sadique Nomani**

Computer Science and Engineering Student

---

If you find this project useful for learning, feel free to explore the code and suggest improvements.
