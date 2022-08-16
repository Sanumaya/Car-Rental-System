from email.policy import default
from django.db import models

# Create your models here.
class StudentDetail(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    is_verified = models.BooleanField(null=True, default=False)
    verification_code = models.CharField(max_length=8)
class Meta:
    db_table = "student_detail"