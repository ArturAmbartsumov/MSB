from django.db import models
from ckeditor.fields import RichTextField
from photologue.models import Photo, Gallery
import datetime

#http://djbook.ru/rel1.6/ref/models/fields.html

class Departments(models.Model):
	short_name = models.CharField(max_length=50, unique = True)
	name = models.CharField(max_length=250)
	description = models.TextField(blank=True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	article = models.ManyToManyField('Articles', blank = True)
	template = models.CharField(max_length=50, default='department.html')
	def __unicode__(self):
		return self.short_name

class Projects(models.Model):
	short_name = models.CharField(max_length=50, unique = True)
	name = models.CharField(max_length=250)
	description = models.TextField()
	department = models.ForeignKey(Departments, blank=True, null=True, on_delete=models.SET_NULL)
	article = models.ManyToManyField('Articles', blank = True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	content = RichTextField()
	template = models.CharField(max_length=50, default='project.html')
	def __unicode__(self):
		return self.short_name

class Articles(models.Model):
	short_name = models.CharField(max_length=50, unique = True)
	title = models.CharField(max_length=250)
	subtext = models.CharField(max_length=250, blank = True)
	author = models.CharField(max_length=250)
	pub_date = models.DateTimeField(default=datetime.datetime.now())
	isFavorite = models.BooleanField(default=True)
	description = RichTextField()
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	content = RichTextField()
	template = models.CharField(max_length=50, default='article.html')
	def __unicode__(self):
		return self.short_name

class News(models.Model):
	title = models.CharField(max_length=250)
	isFavorite = models.BooleanField(default=True)
	description = models.TextField(blank=True)
	pub_date = models.DateTimeField(default=datetime.datetime.now())
	article = models.ManyToManyField(Articles, blank = True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	content = RichTextField()
	template = models.CharField(max_length=50, default='news.html')
	def __unicode__(self):
		return self.title

class AboutBMSTU(models.Model):
	title = models.CharField(max_length=250)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	article = models.ManyToManyField(Articles, blank = True)
	history_title = models.CharField(max_length=250)
	history_text = models.TextField(blank=True)
	history_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	history_gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	nowadays_title = models.CharField(max_length=250)
	nowadays_text = models.TextField(blank=True)
	nowadays_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	graduates = models.ManyToManyField('Persons', blank = True)
	tree_title = models.CharField(max_length=250)
	tree_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	def __unicode__(self):
		return self.title

class Persons(models.Model):
	full_name = models.CharField(max_length=250)
	text = models.TextField(blank=True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	def __unicode__(self):
		return self.full_name

class Contacts(models.Model):
	title = models.CharField(max_length=250)
	photo_map = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	phone_number = models.CharField(max_length=250, blank=True)
	adress = models.CharField(max_length=250, blank=True)
	contact_information = models.TextField(blank=True)
	contactees = models.ManyToManyField(Persons, blank = True)
	def __unicode__(self):
		return self.title





















