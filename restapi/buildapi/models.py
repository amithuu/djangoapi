from django.db import models

# Create your models here.
class CourseList(models.Model):
    Course_Name = models.CharField(max_length=30)
    Language = models.CharField(max_length=20)
    Price = models.CharField(max_length=10)

    def __str__(self):
        return self.Course_Name


