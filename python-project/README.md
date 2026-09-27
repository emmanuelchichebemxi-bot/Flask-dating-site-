# Python Project

A small Python project with a `src` layout, a command-line entry point, a
minimal Flask application, and pytest tests.

## Requirements

- Python 3.11 or newer

## Run

From the project root:

```bash
cd python-project
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m python_project
python -m python_project Ada
```

The installed command is also available as:

```bash
python-project Ada
```

## Run the Flask application

From the `python-project` directory:

```bash
python app.py
```

The application listens on `http://localhost:5000` by default. It exposes:

- `GET /` — welcome message
- `GET /health` — health status

## Run with Docker

Build the image from the `python-project` directory:

```bash
docker build -t python-flask-app .
```

Run the container:

```bash
docker run --rm -p 5000:5000 python-flask-app
```

Then open `http://localhost:5000`.

## Test

```bash
python -m pip install pytest
python -m pytest
```

## Structure

```text
python-project/
├── pyproject.toml
├── app.py
├── README.md
├── src/
│   └── python_project/
│       ├── __init__.py
│       └── main.py
└── tests/
    ├── test_app.py
    └── test_main.py
```