from __future__ import unicode_literals

from django.db import models

class Options(models.Model):
	option_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
	    return self.option_text
	    
class Blog(models.Model):
	blog_text = models.CharField(max_length=10000)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.blog_text