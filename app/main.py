from fastapi import FastAPI
from faker import Faker
from fastapi.middleware.cors import CORSMiddleware
from app import model
from typing import List



app = FastAPI(
    title ='Data Generator'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

faker = Faker()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/getData', response_model=List[model.GenerateData])
async def generateData():
 data = []
 for _ in range(100):
    name = faker.name()
    job = faker.job()
    phone_number = str(faker.phone_number())
    company= faker.company()
    account =  faker.credit_card_number()
    swift = faker.swift(length=11, primary=True)
    balance = faker.pricetag()
    code =  faker.currency_code()

    person = {
        'name': name,
        'job': job,
        'number': phone_number,
        'company': company,
        'account': account,
        'swift': swift,
        'balance': balance,
        'code': code

    }
    data.append(person)
   
 return data