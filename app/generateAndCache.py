import functools
from faker import Faker
faker = Faker()

@functools.lru_cache(maxsize=128)
def generateDataAndCache():
    print('generating and Caching Data')
    data = []
    for _ in range(2000):
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
            'phone_number': phone_number,
            'company': company,
            'account': account,
            'swift': swift,
            'balance': balance,
            'code': code

        }
        data.append(person)
   
    return data