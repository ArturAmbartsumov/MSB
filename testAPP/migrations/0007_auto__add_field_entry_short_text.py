# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.short_text'
        db.add_column(u'testAPP_entry', 'short_text',
                      self.gf('redactor.fields.RedactorField')(default='none'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entry.short_text'
        db.delete_column(u'testAPP_entry', 'short_text')


    models = {
        u'testAPP.entry': {
            'Meta': {'object_name': 'Entry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_text': ('redactor.fields.RedactorField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['testAPP']