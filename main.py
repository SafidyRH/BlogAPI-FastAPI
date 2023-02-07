from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blogy, usera, authentification



app  = FastAPI()


models.Base.metadata.create_all(engine)


app.include_router(authentification.router)
app.include_router(blogy.router)
app.include_router(usera.router)


