# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Graduates'
        db.delete_table(u'main_graduates')

        # Adding model 'Contacts'
        db.create_table(u'main_contacts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('photo_map', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['photologue.Photo'])),
            ('contact_information', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'main', ['Contacts'])

        # Adding M2M table for field contactees on 'Contacts'
        m2m_table_name = db.shorten_name(u'main_contacts_contactees')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contacts', models.ForeignKey(orm[u'main.contacts'], null=False)),
            ('persons', models.ForeignKey(orm[u'main.persons'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contacts_id', 'persons_id'])

        # Adding model 'Persons'
        db.create_table(u'main_persons', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['photologue.Photo'])),
        ))
        db.send_create_signal(u'main', ['Persons'])

        # Removing M2M table for field graduate on 'AboutBMSTU'
        db.delete_table(db.shorten_name(u'main_aboutbmstu_graduate'))

        # Adding M2M table for field graduates on 'AboutBMSTU'
        m2m_table_name = db.shorten_name(u'main_aboutbmstu_graduates')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aboutbmstu', models.ForeignKey(orm[u'main.aboutbmstu'], null=False)),
            ('persons', models.ForeignKey(orm[u'main.persons'], null=False))
        ))
        db.create_unique(m2m_table_name, ['aboutbmstu_id', 'persons_id'])


    def backwards(self, orm):
        # Adding model 'Graduates'
        db.create_table(u'main_graduates', (
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photologue.Photo'], null=True, on_delete=models.SET_NULL, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'main', ['Graduates'])

        # Deleting model 'Contacts'
        db.delete_table(u'main_contacts')

        # Removing M2M table for field contactees on 'Contacts'
        db.delete_table(db.shorten_name(u'main_contacts_contactees'))

        # Deleting model 'Persons'
        db.delete_table(u'main_persons')

        # Adding M2M table for field graduate on 'AboutBMSTU'
        m2m_table_name = db.shorten_name(u'main_aboutbmstu_graduate')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aboutbmstu', models.ForeignKey(orm[u'main.aboutbmstu'], null=False)),
            ('graduates', models.ForeignKey(orm[u'main.graduates'], null=False))
        ))
        db.create_unique(m2m_table_name, ['aboutbmstu_id', 'graduates_id'])

        # Removing M2M table for field graduates on 'AboutBMSTU'
        db.delete_table(db.shorten_name(u'main_aboutbmstu_graduates'))


    models = {
        u'main.aboutbmstu': {
            'Meta': {'object_name': 'AboutBMSTU'},
            'article': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            'graduates': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Persons']", 'symmetrical': 'False', 'blank': 'True'}),
            'history_gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            'history_photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'history_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'history_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nowadays_photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'nowadays_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nowadays_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tree_photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'tree_title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.articles': {
            'Meta': {'object_name': 'Articles'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFavorite': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'subtext': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'article.html'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.contacts': {
            'Meta': {'object_name': 'Contacts'},
            'contact_information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contactees': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Persons']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo_map': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.departments': {
            'Meta': {'object_name': 'Departments'},
            'article': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'department.html'", 'max_length': '50'})
        },
        u'main.news': {
            'Meta': {'object_name': 'News'},
            'article': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFavorite': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'news.html'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.persons': {
            'Meta': {'object_name': 'Persons'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'main.projects': {
            'Meta': {'object_name': 'Projects'},
            'article': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['main.Departments']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'project.html'", 'max_length': '50'})
        },
        u'photologue.gallery': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Gallery'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'galleries'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['photologue.Photo']"}),
            'tags': ('photologue.models.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'photologue.photo': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('photologue.models.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['main']