from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.email)
