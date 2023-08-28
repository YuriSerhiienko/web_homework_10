from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=200)
    born_date = models.DateField()
    born_location = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        app_label = "app_hm10"

    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    text = models.TextField()

    class Meta:
        app_label = "app_hm10"
