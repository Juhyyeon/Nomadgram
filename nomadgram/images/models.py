from django.db import models

# Create your models here.
# auto_now_add : make new model this time save (1 time)
# auto_now : refresh
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Images(TimeStampModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()


class Comment(TimeStampModel):
    message = models.TextField()
    