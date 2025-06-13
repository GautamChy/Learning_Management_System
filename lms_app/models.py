from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model

class InstructorProfile(models.Model):
    InstructorName = models.CharField(max_length = 110)
    bio = models.TextField()
    
    def __str__(self):
        return f"{self.InstructorName}"
    
class Assessment(models.Model):
    title = models.CharField(max_length=255)
    description =models.TextField()
    
    def __str__(self):
        return f"{self.title}"
class CourseList(models.Model):
    ROLE_CHOICES = [
    ('easy', 'Easy'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard'),
]
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE)
    difficulty_level = models.CharField(max_length=50,choices = ROLE_CHOICES )
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.name}"
    
class StudentRecord(models.Model):
    name = models.CharField(max_length=105)
    course = models.ForeignKey(CourseList,on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,null=True,blank=True)
    complete_assessment = models.BooleanField(default = False)
    progress = models.IntegerField(default=0,help_text="Percentage completed(0-100)")
    
    def __str__(self):
        return f"{self.name}"
class SponsershipDetail(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('approved','Approved'),
        ('completed','Completed'),
    ]
    students = models.ForeignKey(StudentRecord,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices= STATUS_CHOICES,default='pending')
    
    
    def __str__(self):
        return f"{self.students}-{self.status}"
    
    