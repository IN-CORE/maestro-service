# Maestro Service
Service to manage playbooks

## Configuration Guide

### Pre-requisites
- Python 3.9
- Install poetry: `pip install poetry`

### Run
Install packages:
`poetry install`

### Setup Environment

Look at env-example for an example environment file and update parameters with your database settings.
For example:

```
#!/bin/bash

export POSTGRES_SERVER=localhost
export POSTGRES_USER=maestro
export POSTGRES_PASSWORD=maestro
export POSTGRES_DB=maestro
export POSTGRES_PORT=5432
export ROUTER_PREFIX=/maestro
```

Run:
`uvicorn app.main:app --reload`

You should be able to run: 
http://localhost:8000/ for base route that return welcome message
http://localhost:8000/docs for swagger docs

## Docker

### Build Docker container

docker build --tag incore/maestro-service:latest .

### Run Docker container
See Setup Environment section for populating the example-env

To run the container:
docker run -p 8000:8000 --env-file env-example incore/maestro-service:latest

