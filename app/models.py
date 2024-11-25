from django.db import models
from django.contrib.auth.models import User

class feedback(models.Model):
    username = models.CharField(max_length= 70)
    name = models.CharField(max_length= 70)
    designation = models.CharField(max_length= 70)
    q1 = models.CharField(max_length= 50)
    q2 = models.CharField(max_length= 50)
    q3 = models.CharField(max_length= 50)
    q4 = models.CharField(max_length= 50)
    q5 = models.CharField(max_length= 50)
    q6 = models.CharField(max_length= 50)
    q7 = models.CharField(max_length= 50)
    q8 = models.CharField(max_length= 50)
    q9 = models.CharField(max_length= 50)
    q10 = models.CharField(max_length= 50)
    q11 = models.CharField(max_length= 50)
    q12 = models.CharField(max_length= 50)
    q13 = models.CharField(max_length= 50)
    q14 = models.CharField(max_length= 50)
    q15 = models.CharField(max_length= 50)
    qus_pred = models.CharField(max_length= 50)
    feedback = models.CharField(max_length= 500)
    feedback_pred = models.CharField(max_length= 50)
    happiness_index = models.CharField(max_length= 50)
    date = models.DateField()

    def __str__(self):
        return self.username
    
# Create your models here.
class profile_data(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    designation = models.CharField(max_length= 50)
    
    def __str__(self):
        return str(self.user)
