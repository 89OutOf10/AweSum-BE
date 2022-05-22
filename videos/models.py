from django.db import models


class Video(models.Model):
    videoid = models.CharField(max_length=50, unique=True)
    transcript = models.TextField()


class Subtitle(models.Model):
    videoid = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    time = models.TextField()
    sub_num = models.IntegerField(default=1, null=True)