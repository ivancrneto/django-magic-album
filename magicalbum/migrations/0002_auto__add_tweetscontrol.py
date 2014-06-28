# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TweetsControl'
        db.create_table(u'magicalbum_tweetscontrol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('since_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'magicalbum', ['TweetsControl'])


    def backwards(self, orm):
        # Deleting model 'TweetsControl'
        db.delete_table(u'magicalbum_tweetscontrol')


    models = {
        u'magicalbum.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pictures': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        },
        u'magicalbum.tweetscontrol': {
            'Meta': {'object_name': 'TweetsControl'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'since_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['magicalbum']