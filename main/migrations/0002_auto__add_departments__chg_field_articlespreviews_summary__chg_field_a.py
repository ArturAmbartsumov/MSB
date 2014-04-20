# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Departments'
        db.create_table(u'main_departments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('about', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'main', ['Departments'])


        # Changing field 'ArticlesPreviews.summary'
        db.alter_column(u'main_articlespreviews', 'summary', self.gf('ckeditor.fields.RichTextField')())
        # Adding M2M table for field department on 'Articles'
        m2m_table_name = db.shorten_name(u'main_articles_department')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articles', models.ForeignKey(orm[u'main.articles'], null=False)),
            ('departments', models.ForeignKey(orm[u'main.departments'], null=False))
        ))
        db.create_unique(m2m_table_name, ['articles_id', 'departments_id'])


        # Changing field 'Articles.content'
        db.alter_column(u'main_articles', 'content', self.gf('ckeditor.fields.RichTextField')())

    def backwards(self, orm):
        # Deleting model 'Departments'
        db.delete_table(u'main_departments')


        # Changing field 'ArticlesPreviews.summary'
        db.alter_column(u'main_articlespreviews', 'summary', self.gf('redactor.fields.RedactorField')())
        # Removing M2M table for field department on 'Articles'
        db.delete_table(db.shorten_name(u'main_articles_department'))


        # Changing field 'Articles.content'
        db.alter_column(u'main_articles', 'content', self.gf('redactor.fields.RedactorField')())

    models = {
        u'main.articles': {
            'Meta': {'object_name': 'Articles'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'department': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Departments']", 'symmetrical': 'False'}),
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
        }
    }

    complete_apps = ['main']