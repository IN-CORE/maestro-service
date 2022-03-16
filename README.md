# Maestro Service
Service to manage playbooks

## Configuration Guide

### Pre-requisites
- Python 3.8 or 3.9
- Install poetry: `pip install poetry`

### Run
Install packages:
`poetry install`

Run:
`uvicorn app.main:app --reload`

You should be able to run: 
http://localhost:8000/ for base route that return welcome message
http://localhost:8000/docs for swagger docs
