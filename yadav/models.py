from django.db import models

class Hello(models.Model):
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=200)
	image=models.ImageField(upload_to='yadav/images/')
	url = models.URLField(blank=True)
