# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.new_field'
        db.add_column(u'testAPP_entry', 'new_field',
                      self.gf('django.db.models.fields.CharField')(default='null', max_length=250),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entry.new_field'
        db.delete_column(u'testAPP_entry', 'new_field')


    models = {
        u'testAPP.entry': {
            'Meta': {'object_name': 'Entry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_field': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'short_text': ('redactor.fields.RedactorField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['testAPP']