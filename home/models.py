from django.db import models
from django.utils.timezone import now

# Create your models here.

class College(models.Model):
    college_name = models.CharField(max_length=100)
    #To print normally with names or else numbers will be printed
    #def __str__(self):
     #   return self.college_name

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)



class Student(models.Model):
    student_id = models.CharField(max_length=100,null = True, blank = True)
    college = models.ForeignKey(College, on_delete = models.CASCADE)
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

    #created_at = models.DateTimeField(auto_now=True)
    #updated_at = models.DateTimeField(auto_now_add=True)
    #If we open flikart.com and after that if we select any product
    # it will redirect to that page.,the text after flikart.com is slugfield
    #slug = models.SlugField()
    #uid = models.UUIDField()

    def __str__(self) -> str:
        return self.name 
    
    #zfill is used to get zeroes like 0001 , the number we passed inside zfill

    def save(self,*args,**kwargs):
        if not self.student_id:
            last_student_id = 1
            print('Hi')
            last_object = Student.objects.last()
            if last_object:
                last_student_id = last_object.id 
            student_id = f"STU-{str(last_student_id).zfill(5)}"
            self.student_id = student_id 
        
        else:
            self.update()

        super(Student, self).save(*args, **kwargs)

    def update(self,*args,**kwargs):
        print("Update method called")
        super(Student,self).update(*args,**kwargs)

