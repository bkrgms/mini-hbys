import psycopg2
import os
from dotenv import load_dotenv
from faker import Faker
import random
import csv 
load_dotenv()
fake = Faker('tr_TR')

patients = []

connection = psycopg2.connect(
    host=os.getenv('DB_HOST'),
    database=os.getenv('DB_DATABASE'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)

cursor = connection.cursor()

for i in range(10000):
    full_name = fake.name()
    birth_date = fake.date_of_birth(minimum_age=1,maximum_age=99)
    gender = fake.random_element(elements=('male','female'))
    cursor.execute(
        "INSERT INTO patients (full_name, birth_date, gender) VALUES(%s,%s,%s)",
        (full_name,birth_date,gender)
    )

connection.commit()

cursor.execute("select full_name, birth_date, gender from patients")
patients = cursor.fetchall()
os.makedirs('data',exist_ok=True)
with open("data/patients.csv",'w',newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["full_name","birth_date","gender"])
    writer.writerows(patients)

cursor.close()
connection.close()
