from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)


class Student(models.Model):
    department = models.ForeignKey(Department,
                                   models.CASCADE,
                                   models.SET_NULL,
                                   models.SET_DEFAULT,
                                   models.PROTECT)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
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
    student_registration = models.DateTimeField()
    percentage = models.FloatField(default= 10)
    student_image = models.ImageField(upload_to = "images/students/")
    file = models.FileField(upload_to="images/students/")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #If we open flikart.com and after that if we select any product
    # it will redirect to that page.,the text after flikart.com is slugfield
    slug = models.SlugField()
    uid = models.UUIDField()
