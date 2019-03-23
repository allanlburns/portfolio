from django.db import models

class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)
	url = models.URLField(max_length=200, default='#')
	github_url = models.URLField(max_length=200, default='#')


	def __str__(self):
		return self.summary[:100]