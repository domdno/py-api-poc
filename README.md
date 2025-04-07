# FastAPI Server for Proof of Concept

FastAPI server created as a proof of concept. To be used as a project template and to test new ideas.

- API version: 1.0.0

## Requirements

Python >= 3.12

## Local Install & Run

From the root directory, please execute the following:

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Docker Install & Run

To run as a container, please execute the following:

```bash
docker-compose up --build
```
