from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField()
    birth = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.lastName


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
