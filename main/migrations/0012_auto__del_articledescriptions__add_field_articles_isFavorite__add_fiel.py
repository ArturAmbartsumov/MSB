# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ArticleDescriptions'
        db.delete_table(u'main_articledescriptions')

        # Adding M2M table for field article on 'Departments'
        m2m_table_name = db.shorten_name(u'main_departments_article')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('departments', models.ForeignKey(orm[u'main.departments'], null=False)),
            ('articles', models.ForeignKey(orm[u'main.articles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['departments_id', 'articles_id'])

        # Adding field 'Articles.isFavorite'
        db.add_column(u'main_articles', 'isFavorite',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Articles.description'
        db.add_column(u'main_articles', 'description',
                      self.gf('ckeditor.fields.RichTextField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Removing M2M table for field department on 'Articles'
        db.delete_table(db.shorten_name(u'main_articles_department'))

        # Adding field 'Projects.content'
        db.add_column(u'main_projects', 'content',
                      self.gf('ckeditor.fields.RichTextField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding M2M table for field article on 'Projects'
        m2m_table_name = db.shorten_name(u'main_projects_article')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projects', models.ForeignKey(orm[u'main.projects'], null=False)),
            ('articles', models.ForeignKey(orm[u'main.articles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projects_id', 'articles_id'])

        # Adding M2M table for field article on 'News'
        m2m_table_name = db.shorten_name(u'main_news_article')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('news', models.ForeignKey(orm[u'main.news'], null=False)),
            ('articles', models.ForeignKey(orm[u'main.articles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['news_id', 'articles_id'])


    def backwards(self, orm):
        # Adding model 'ArticleDescriptions'
        db.create_table(u'main_articledescriptions', (
            ('article', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Articles'], unique=True)),
            ('description', self.gf('ckeditor.fields.RichTextField')()),
            ('isFavorite', self.gf('django.db.models.fields.BooleanField')(default=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'main', ['ArticleDescriptions'])

        # Removing M2M table for field article on 'Departments'
        db.delete_table(db.shorten_name(u'main_departments_article'))

        # Deleting field 'Articles.isFavorite'
        db.delete_column(u'main_articles', 'isFavorite')

        # Deleting field 'Articles.description'
        db.delete_column(u'main_articles', 'description')

        # Adding M2M table for field department on 'Articles'
        m2m_table_name = db.shorten_name(u'main_articles_department')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articles', models.ForeignKey(orm[u'main.articles'], null=False)),
            ('departments', models.ForeignKey(orm[u'main.departments'], null=False))
        ))
        db.create_unique(m2m_table_name, ['articles_id', 'departments_id'])

        # Deleting field 'Projects.content'
        db.delete_column(u'main_projects', 'content')

        # Removing M2M table for field article on 'Projects'
        db.delete_table(db.shorten_name(u'main_projects_article'))

        # Removing M2M table for field article on 'News'
        db.delete_table(db.shorten_name(u'main_news_article'))


    models = {
        u'main.articles': {
            'Meta': {'object_name': 'Articles'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photologue.Gallery']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFavorite': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photologue.Photo']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'subtext': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'article.html'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.departments': {
            'Meta': {'object_name': 'Departments'},
            'article': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photologue.Gallery']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photologue.Photo']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'department.html'", 'max_length': '50'})
        },
        u'main.news': {
            'Meta': {'object_name': 'News'},
            'article': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photologue.Gallery']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFavorite': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photologue.Photo']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'news.html'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.projects': {
            'Meta': {'object_name': 'Projects'},
            'article': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Departments']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photologue.Gallery']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photologue.Photo']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
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