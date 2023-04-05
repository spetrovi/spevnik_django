from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    birth_date = models.DateTimeField('birth date')
    def __str__(self):
        return self.name + ' ' + self.surname
    

    
