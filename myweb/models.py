from django.db import models



class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=300)
    desc = models.TextField()


    def __str__(self):
        return f'{self.name} - {self.img}   '


