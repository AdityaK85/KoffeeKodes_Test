from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class MyUser(AbstractUser):
    role = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        permissions = (
            ('can_add_users', 'Can add users'),
            ('can_schedule_interview', 'Can schedule interviews')
        )


class InterviewMaster(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    candidate_name = models.CharField(max_length=255,blank=True, null=True)
    interview_date = models.DateTimeField(blank=True, null=True)
    interviewer = models.ForeignKey(MyUser, on_delete=models.CASCADE,blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_dt = models.DateField(blank=True, null=True)

