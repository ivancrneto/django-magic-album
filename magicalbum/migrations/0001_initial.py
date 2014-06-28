# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table(u'magicalbum_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pictures', self.gf('jsonfield.fields.JSONField')(default={})),
        ))
        db.send_create_signal(u'magicalbum', ['Album'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table(u'magicalbum_album')


    models = {
        u'magicalbum.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pictures': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        }
    }

    complete_apps = ['magicalbum']