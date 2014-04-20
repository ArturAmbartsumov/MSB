# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Entry.title'
        db.delete_column(u'testAPP_entry', 'title')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Entry.title'
        raise RuntimeError("Cannot reverse this migration. 'Entry.title' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Entry.title'
        db.add_column(u'testAPP_entry', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=250),
                      keep_default=False)


    models = {
        u'testAPP.entry': {
            'Meta': {'object_name': 'Entry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_text': ('redactor.fields.RedactorField', [], {})
        }
    }

    complete_apps = ['testAPP']