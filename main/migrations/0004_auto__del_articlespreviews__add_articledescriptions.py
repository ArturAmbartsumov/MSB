# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ArticlesPreviews'
        db.delete_table(u'main_articlespreviews')

        # Adding model 'ArticleDescriptions'
        db.create_table(u'main_articledescriptions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Articles'], unique=True)),
            ('summary', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal(u'main', ['ArticleDescriptions'])


    def backwards(self, orm):
        # Adding model 'ArticlesPreviews'
        db.create_table(u'main_articlespreviews', (
            ('article', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Articles'], unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('summary', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal(u'main', ['ArticlesPreviews'])

        # Deleting model 'ArticleDescriptions'
        db.delete_table(u'main_articledescriptions')


    models = {
        u'main.articledescriptions': {
            'Meta': {'object_name': 'ArticleDescriptions'},
            'article': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Articles']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('ckeditor.fields.RichTextField', [], {})
        },
        u'main.articles': {
            'Meta': {'object_name': 'Articles'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'department': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Departments']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
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