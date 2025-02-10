from .models import * 
from faker import Faker
import random
#from home.models import Student 


fake = Faker() 


def seedDB(num_records = 10):
    for record in range(0,num_records):
        college = College.objects.all().order_by('?')[0]
        department = Department.objects.all().order_by('?')[0]
        skills = Skills.objects.all().order_by('?')
        name = fake.name()
        age = random.randint(18,34)
        genders = ['Male','Female']
        gender = random.choice(genders)
        phone_number = random.randint(1000000000,9999999999)
        student_bio = fake.sentence()
        email = fake.email()
        date_of_birth = fake.date_of_birth(minimum_age=18,maximum_age=34)
        student = Student.objects.create(
            name = name ,
            age =  age,
            gender = gender, 
            phone_number = phone_number, 
            student_bio = student_bio ,
            email = email ,
            date_of_birth = date_of_birth,
            college = college,
            department =  department, 
        )
        for skill in skills[:2]:
            student.skills.add(skill)
            student.save()

