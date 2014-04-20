# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Entry.short_text'
        db.delete_column(u'testAPP_entry', 'short_text')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Entry.short_text'
        raise RuntimeError("Cannot reverse this migration. 'Entry.short_text' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Entry.short_text'
        db.add_column(u'testAPP_entry', 'short_text',
                      self.gf('redactor.fields.RedactorField')(),
                      keep_default=False)


    models = {
        u'testAPP.entry': {
            'Meta': {'object_name': 'Entry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['testAPP']