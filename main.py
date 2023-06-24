from fastapi import FastAPI
from db import models
from db.database import engine

app = FastAPI()


models.Base.metadata.create_all(engine)