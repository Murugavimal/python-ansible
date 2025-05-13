from fastapi import FastAPI
import userapp , userapp_readonly, models
from  database import engine


models.Base.metadata.create_all(bind=engine)

app= FastAPI()

app.include_router(userapp.router)

app.include_router(userapp_readonly.router)