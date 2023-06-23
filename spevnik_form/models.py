from django.db import models


class Song(models.Model):
    def __str__(self):
        metadata = models.OneToOneField(Metadata, on_delete=models.CASCADE)
        stanzas = models.ManyToManyField(Stanza)
        return f"Song {self.metadata.title}"


class Stanza(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    def __str__(self):
        return f"Stanza {self.id}"


class Verse(models.Model):
    stanza = models.ForeignKey(Stanza, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Author(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    birth_date = models.DateTimeField("birth date")

    def __str__(self):
        return self.name + " " + self.surname
        
class Metadata(models.Model):
    title = models.CharField(max_length=200)
    gathered_date = models.DateTimeField("date gathered")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rhytm = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
    song = models.OneToOneField(Song, on_delete=models.CASCADE)
    def __str__(self):
        return f"Metadata {self.id}"


