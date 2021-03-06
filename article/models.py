from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 100)                  # blog title
	category = models.CharField(max_length = 50, blank = True)  # blog tag
	date_time = models.DateTimeField(auto_now_add = True)       # blog date_time
	content = models.TextField(blank = True, null = True)       # blog content

# Get the URL and convert it to the url representation format

	def get_absolute_url(self):
		path = reverse('detail', kwargs={'id':self.id})
		return "http://127.0.0.1:8000%s" % path

	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-date_time']
