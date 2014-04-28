from django.db import models
from ckeditor.fields import RichTextField
from photologue.models import Photo, Gallery

class Departments(models.Model):
	short_name = models.CharField(max_length=50, unique = True)
	name = models.CharField(max_length=250)
	about = models.TextField(blank=True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL)
	gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL)
	template = models.CharField(max_length=50, default='department.html')
	def __unicode__(self):
		return self.short_name

class Projects(models.Model):
	short_name = models.CharField(max_length=50, unique = True)
	name = models.CharField(max_length=250)
	about = models.TextField()
	department = models.ForeignKey(Departments, blank=True, null=True, on_delete=models.SET_NULL)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL)
	gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL)
	template = models.CharField(max_length=50, default='project.html')
	def __unicode__(self):
		return self.short_name

class Articles(models.Model):
	short_name = models.CharField(max_length=50, unique = True)
	title = models.CharField(max_length=250)
	subtext = models.CharField(max_length=250, blank = True)
	department = models.ManyToManyField(Departments, blank = True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL)
	gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL)
	content = RichTextField()
	template = models.CharField(max_length=50, default='article.html')
	def __unicode__(self):
		return self.short_name

class ArticleDescriptions(models.Model):
	article = models.OneToOneField(Articles)
	summary = RichTextField()
	def __unicode__(self):
		return self.article.short_name