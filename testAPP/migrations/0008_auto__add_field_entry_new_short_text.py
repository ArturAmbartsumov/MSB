# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.new_short_text'
        db.add_column(u'testAPP_entry', 'new_short_text',
                      self.gf('redactor.fields.RedactorField')(default='\xd0\xbd\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entry.new_short_text'
        db.delete_column(u'testAPP_entry', 'new_short_text')


    models = {
        u'testAPP.entry': {
            'Meta': {'object_name': 'Entry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_short_text': ('redactor.fields.RedactorField', [], {}),
            'short_text': ('redactor.fields.RedactorField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['testAPP']