from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    birth_date = models.DateTimeField("birth date")

    def __str__(self):
        return self.name + " " + self.surname


class Song(models.Model):
    metadata = models.OneToOneField("Metadata", on_delete=models.CASCADE)

    def __str__(self):
        return f"Song {self.metadata.title}"


class Metadata(models.Model):
    title = models.CharField(max_length=200)
    gathered_date = models.DateTimeField("date gathered")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rhythm = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    song = models.OneToOneField(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"Metadata {self.id}"


class Stanza(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"Stanza {self.id}"


class Verse(models.Model):
    stanza = models.ForeignKey(Stanza, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
