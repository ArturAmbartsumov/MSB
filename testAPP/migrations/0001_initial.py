# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table(u'testAPP_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('short_text', self.gf('redactor.fields.RedactorField')()),
        ))
        db.send_create_signal(u'testAPP', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Entry'
        db.delete_table(u'testAPP_entry')


    models = {
        u'testAPP.entry': {
            'Meta': {'object_name': 'Entry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_text': ('redactor.fields.RedactorField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['testAPP']