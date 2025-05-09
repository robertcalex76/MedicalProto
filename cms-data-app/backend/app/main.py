from fastapi import FastAPI
from app.api import endpoints
from app.db import models
from app.db.database import engine

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Include the API routes
app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the CMS Nursing Home Data API!"}