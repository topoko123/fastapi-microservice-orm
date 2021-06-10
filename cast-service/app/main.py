from fastapi import FastAPI

from app.api.casts import casts


app = FastAPI()

app.include_router(casts, prefix='/api/v1/casts', tags=['Cast'])
