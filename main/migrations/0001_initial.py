# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Articles'
        db.create_table(u'main_articles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content', self.gf('redactor.fields.RedactorField')()),
        ))
        db.send_create_signal(u'main', ['Articles'])

        # Adding model 'ArticlesPreviews'
        db.create_table(u'main_articlespreviews', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Articles'], unique=True)),
            ('summary', self.gf('redactor.fields.RedactorField')()),
        ))
        db.send_create_signal(u'main', ['ArticlesPreviews'])


    def backwards(self, orm):
        # Deleting model 'Articles'
        db.delete_table(u'main_articles')

        # Deleting model 'ArticlesPreviews'
        db.delete_table(u'main_articlespreviews')


    models = {
        u'main.articles': {
            'Meta': {'object_name': 'Articles'},
            'content': ('redactor.fields.RedactorField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.articlespreviews': {
            'Meta': {'object_name': 'ArticlesPreviews'},
            'article': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Articles']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('redactor.fields.RedactorField', [], {})
        }
    }

    complete_apps = ['main']