from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    comment = models.CharField(max_length=500) #need to change it to text field
    def __str__(self):
        return self.comment

class FileInput(models.Model):
    CHOICES1=[('encrypt', 'encrypt'),
             ('decrypt', 'decrypt')]
    key = models.CharField(max_length=24, validators=[MinLengthValidator(24)])
    file = models.ImageField(null=False)
    choice = models.CharField(choices=CHOICES1, max_length=20)
