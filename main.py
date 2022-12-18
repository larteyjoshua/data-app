from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import model
from typing import List
from fastapi import FastAPI, HTTPException
from app.generateAndCache import generateDataAndCache
import random



app = FastAPI(
    title ='Data Generator'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    generateDataAndCache()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/v1/accounts/all', response_model=List[model.GenerateData])
async def get_all_data():
    response = generateDataAndCache() 
    return response

@app.get('/v1/accounts/{total_number}', response_model=List[model.GenerateData])
async def get_data_with_parameter(total_number:int):
 if total_number > 0 and total_number < 2001:
    data = generateDataAndCache()
    response = random.sample(data, total_number)
    return response
 else:
    raise HTTPException(status_code=418, detail="Enter a number between 0 and 2001")

#     {
#         "name": "faker-data",
#         "id": "e69d9dcd-1402-49f2-aa24-d6ee3eb31e21",
#         "project": "a0kt1j9c",
#         "runtime": "python3.9",
#         "endpoint": "https://h0mdd0.deta.dev",
#         "region": "eu-central-1",
#         "visor": "disabled",
#         "http_auth": "disabled"
# }