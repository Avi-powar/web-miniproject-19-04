from django.db import models # type: ignore

# Create your models here.
class Contact(models.Model):
    name_id = models.CharField(max_length=20)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    def __str__(self):
        return self.name_id