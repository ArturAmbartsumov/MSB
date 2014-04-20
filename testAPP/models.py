from django.db import models
from redactor.fields import RedactorField, RedactorEditor
import PIL
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill
from ckeditor.fields import RichTextField

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    short_text = RedactorField(verbose_name=u'Text',
    	redactor_options={'lang': 'en', 'focus': 'true'},
    	upload_to='tmp',
    	allow_file_upload=True,
    	allow_image_upload=True)

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')

class Jobseeker(models.Model):
	photo = models.ImageField(verbose_name=u'Poster',upload_to='image', max_length=256, blank=True, null=True)
	photo_small =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(50, 50)], format='JPEG', options={'quality': 90})
	photo_medium =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(300, 200)], format='JPEG', options={'quality': 90})
	photo_big =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(640, 480)], format='JPEG', options={'quality': 90})

class Post(models.Model):
	content = RichTextField()