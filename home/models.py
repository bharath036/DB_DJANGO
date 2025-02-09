from django.db import models
from django.utils.timezone import now

# Create your models here.

class College(models.Model):
    college_name = models.CharField(max_length=100)
    #To print normally with names or else numbers will be printed
    def __str__(self):
        return self.college_name

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)

class Student(models.Model):
    college = models.OneToOneField(College, on_delete = models.CASCADE)
    department = models.ForeignKey (Department,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)  

    name = models.CharField(max_length = 100)
    age = models.IntegerField(null = True , blank = True)
    gender = models.CharField(max_length=10,choices=(
        ("Male","Male"),
        ("Female","Female")), default="Male"
    )
    phone_number = models.CharField(max_length=10, null=True,blank=True)
    #In textfield, we can pass  "editable" parameter value as TRUE or False
    #if editable is false.., once the field is edied it can't be edited again
    student_bio = models.TextField()
    email = models.TextField()
    date_of_birth = models.DateField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #If we open flikart.com and after that if we select any product
    # it will redirect to that page.,the text after flikart.com is slugfield
    #slug = models.SlugField()
    #uid = models.UUIDField()


'''
student = Student.objects.create(
    name = "Akash Gupta",
    gender = "Male",
    age = 10,
    phone_number = 908953212,
    student_bio = "Hi, I am Akash Gupta",
    email = "Akash@gmail.com",
    date_of_birth =  "2020-11-01",
    college= college,
    department = department
)
'''

'''
colleges = ['IIT DELHI','LPU','MANIPAL','MIT']
departments = ['CS','IT','Mechanical','Civil']
skills = ['Python','English','Reading','Music']
'''