# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Projects'
        db.create_table(u'main_projects', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Departments'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'main', ['Projects'])


    def backwards(self, orm):
        # Deleting model 'Projects'
        db.delete_table(u'main_projects')


    models = {
        u'main.articles': {
            'Meta': {'object_name': 'Articles'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'department': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Departments']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.articlespreviews': {
            'Meta': {'object_name': 'ArticlesPreviews'},
            'article': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Articles']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('ckeditor.fields.RichTextField', [], {})
        },
        u'main.departments': {
            'Meta': {'object_name': 'Departments'},
            'about': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'main.projects': {
            'Meta': {'object_name': 'Projects'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Departments']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['main']