from fastapi import FastAPI


app = FastAPI(title="Maestro API")


@app.get("/")
def index():
    return {"message": "Welcome to Maestro service"}
