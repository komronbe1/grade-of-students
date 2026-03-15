from django.db import models
from apps.student.models import Student
from apps.course.models import Course


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return str(self.grade)