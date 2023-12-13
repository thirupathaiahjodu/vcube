from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_id = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    key_features = models.TextField()
    course_details = models.TextField()
    trainer = models.ManyToManyField(Trainer)

    # AutoField for id, no need to set a default value
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.course_name

class Batch(models.Model):
    batch_number = models.CharField(primary_key=True, max_length=100) 
    batch_timings = models.CharField(max_length=100,null=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f"Batch {self.batch_number} - {self.course}"

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    alternative_number=models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    graduation = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    trainer = models.ManyToManyField(Trainer)
    status = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='No')

    def __str__(self):
        return self.name
    
class StudentuserManager(models.Manager):
    def search(self, query):
        return self.filter(
            models.Q(user__username__icontains=query) |
            models.Q(admission_number__icontains=query) |
            models.Q(joining_date__icontains=query) |
            models.Q(batch__batch_number__icontains=query) |  # Correct lookup for ForeignKey field
            models.Q(actual_fees__icontains=query) |
            models.Q(fees_paid__icontains=query) |
            models.Q(course__course_name__icontains=query)   # Correct lookup for ForeignKey field
        )



class Studentuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=True)
    admission_number = models.CharField(max_length=50,default=True)
    joining_date = models.DateField(default=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE,default=True)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    actual_fees = models.DecimalField(max_digits=10, decimal_places=2,default=True)
    fees_paid = models.DecimalField(max_digits=10, decimal_places=2,default=True)
    resume = models.FileField(upload_to='user_resumes/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,default=True)
    objects = StudentuserManager()

    def __str__(self):
        return self.user.username


class Test(models.Model):
    student = models.ForeignKey(Studentuser, on_delete=models.CASCADE)
    test_date = models.DateField()
    present = models.BooleanField(default=False,null=True)
    marks = models.DecimalField(max_digits=8, decimal_places=2, validators=[MaxValueValidator(100)])
    max_marks = models.DecimalField(max_digits=8, decimal_places=2, validators=[MaxValueValidator(100)], default=10)

    def __str__(self):
        return f"Test: {self.pk} - Student: {self.student.user.username}"


class Attendance(models.Model):
    student = models.ForeignKey(Studentuser, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"Attendance: {self.pk} - Student: {self.student.user.username}"

class lab(models.Model):
    student=models.ForeignKey(Studentuser,on_delete=models.CASCADE)
    date=models.DateField()
    present=models.BooleanField(default=False)

class communication(models.Model):
    student=models.ForeignKey(Studentuser,on_delete=models.CASCADE)
    date=models.DateField()
    present=models.BooleanField(default=False)
    topic=models.TextField(null=True)

class softskills(models.Model):
    student=models.ForeignKey(Studentuser,on_delete=models.CASCADE)
    date=models.DateField()
    present=models.BooleanField(default=False)
    topic=models.TextField()




class Interview(models.Model):
    student = models.ForeignKey(Studentuser, on_delete=models.CASCADE)
    interview_date = models.DateField()
    present = models.BooleanField(default=False)
    performance = models.DecimalField(max_digits=4, decimal_places=2,validators=[MaxValueValidator(10)],null=True)
    max_performance = models.DecimalField(max_digits=8, decimal_places=2, validators=[MaxValueValidator(100)], default=10)
    marks=models.DecimalField(max_digits=8,decimal_places=2,validators=[MaxValueValidator(10)],null=True)
    max_marks = models.DecimalField(max_digits=8, decimal_places=2, validators=[MaxValueValidator(100)], default=10)

    def __str__(self):
        return f"Interview: {self.pk} - Student: {self.student.user.username}"

class admissionform(models.Model):
    Email=models.EmailField(unique=True)
    Name=models.CharField(max_length=30)
    Mobile=models.CharField(max_length=12)
    Alternate_Mobile=models.CharField(max_length=12)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    T_Chocies=[
        ('Mr.Srinivas','Mr.Srinivas'),
        ('Mr.Madhukar','Mr.Madhukar'),
        ('Mr.Manohar','Mr.Manohar'),
        ('Mr.Suresh','Mr.Suresh'),
        ('Mr.PVR','Mr.PVR'),
        ('O', 'Other'),
    ]
    Tranier = models.CharField(max_length=20, choices=T_Chocies)
    Mode_of_Traning=models.CharField(max_length=10,choices=[('Offline','Offline'),('Online','Online')])
    Batch_timings=models.CharField(max_length=5)
    DateOfjoining=models.DateField()
    Batch_Number=models.CharField(max_length=5)
    Qulification=models.CharField(max_length=10)
    Work_experience=models.CharField(max_length=10)
    Experience_or_Fresher=models.CharField(max_length=10)
    Backlogs=models.CharField(max_length=5)
    Linked=models.CharField(max_length=50)
    Instagram=models.CharField(max_length=30)
    Image=models.ImageField(upload_to='images/',null=True)
    INTEREST_CHOICES = [
        ('EASIER', 'Because this is easier than other courses.'),
        ('INTEREST', 'I absorbed myself I am quite interested on this course.'),
        ('SUGGESTION', 'My friend suggestion or parents suggestion.'),
        ('DEMAND', 'This course have highest demand in market.'),]
    VCUBE_CHOICES = [
        ('TRAINERS', 'VCUBE have professional trainers and process is good'),
        ('TRENDING', 'VCUBE is trending institute'),
        ('FRIEND', 'My friend suggestion'),
        ('ASSISTANCE', 'Because of 100 % assistance'),
        ]
    EXPECTATIONS_CHOICES = [
        ('PLACEMENTS', '100 % placements'),
        ('KNOWLEDGE', 'Best training and best knowledge on particular course'),
        ('GUIDANCE', 'Best guidance + placement assistance'),
        ('NONE', 'No expectations'),
        ]
    WEAKNESS_CHOICES = [
        ('FEAR', 'Stage fear'),
        ('COMMUNICATION', 'Lack of communication'),
        ('KNOWLEDGE', 'Lack of subject knowledge'),
        ('ALL', 'All the above'),
        ]

    TEST_CHOICES = [('YES', 'Yes, it is'),('NO', 'No'),('UNKNOWN', 'I don’t know'),]

    MOCK_CHOICES = TEST_CHOICES

    HEAR_CHOICES = [('SOCIAL', 'Social media'),('FRIEND', 'Friends reference'),('RANDOM', 'Randomly'),]
    course_interest = models.CharField(max_length=20, choices=INTEREST_CHOICES,blank=False)
    v_cube_reason = models.CharField(max_length=20, choices=VCUBE_CHOICES,blank=False)
    expectations = models.CharField(max_length=20, choices=EXPECTATIONS_CHOICES,blank=False)
    weakness = models.CharField(max_length=20, choices=WEAKNESS_CHOICES,blank=False)
    test_importance = models.CharField(max_length=20, choices=TEST_CHOICES,blank=False)
    mock_value = models.CharField(max_length=20, choices=MOCK_CHOICES,blank=False)
    hear_about_us = models.CharField(max_length=20, choices=HEAR_CHOICES,blank=False)


class jopForm(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    #...add more CHOICES as needed

    current_city = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #acdamic Details
    resume = models.FileField(upload_to='resumes/')
    degree_college = models.CharField(max_length=255)
    passed_out_year = models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    post_graduation = models.CharField(max_length=255, null=True, blank=True)
    pg_degree_college = models.CharField(max_length=255, null=True, blank=True)
    pg_passed_out_year = models.IntegerField(null=True, blank=True)

    # profinal Details
    relevant_experience = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    reporting_person_contact = models.CharField(max_length=255, null=True, blank=True)

    
