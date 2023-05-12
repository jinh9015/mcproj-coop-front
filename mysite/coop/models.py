from django.db import models

# Create your models here.
class coop(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField() 
    create_date = models.DateTimeField()

    def __str__(self):
        return "subject : " +self.subject
   
class coopanswer(models.Model):
    question = models.ForeignKey(coop, on_delete=models.CASCADE)
    content =  models.TextField()
    create_date = models.DateTimeField()