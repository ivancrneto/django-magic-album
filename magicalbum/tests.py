""" Module for Magic Album tests """

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from magicalbum.models import Album
import json


class TestAlbumView(TestCase):
    """ Class for testing Magic Album view """

    def test_status_code(self):
        """ Response status code for album view should be 200 """
        resp = self.client.get(r('magicalbum:album'))
        self.assertEqual(200, resp.status_code)

    def test_no_album(self):
        """ Message the user if there is no album """
        resp = self.client.get(r('magicalbum:album'))
        self.assertContains(resp,
                            'The magic album has not created yet')

    def test_no_picture(self):
        """ Message the user if there is no picture in the album """
        album = Album()
        album.save()
        resp = self.client.get(r('magicalbum:album'))
        self.assertContains(resp,
                            'The magic album has no pictures yet.')

    def test_pictures(self):
        """ Number of pictures in page should match album pictures """
        album = Album()
        album.pictures = [
            {
                'user': 'ivan',
                'picture': 'http://example.com/picture.jpg'
            },
            {
                'user': 'ivan',
                'picture': 'http://example.com/picture.jpg'
            }
        ]

        album.save()
        resp = self.client.get(r('magicalbum:album'))
        self.assertEqual(album.pictures, resp.context['album'].pictures)
        self.assertContains(resp, '<img', len(album.pictures))


class TestAlbumAPI(TestCase):
    """ Class for testing Magic Album API """

    def test_status_code(self):
        """ Response status code for album view should be 200 """
        resp = self.client.get(r('magicalbum:api'))
        self.assertEqual(200, resp.status_code)

    def test_no_album_or_no_picture(self):
        """ Return empty list if there is no album or no picture """

        # no album test
        resp = self.client.get(r('magicalbum:api'))
        resp = json.loads(resp.content)
        self.assertEqual([], resp)

        # no picture test
        album = Album()
        album.save()
        resp = self.client.get(r('magicalbum:api'))
        resp = json.loads(resp.content)
        self.assertEqual([], resp)

    def test_pictures(self):
        """ Pictures in json should match album pictures """
        album = Album()
        album.pictures = [
            {
                'user': 'ivan',
                'picture': 'http://example.com/picture.jpg'
            },
            {
                'user': 'ivan',
                'picture': 'http://example.com/picture.jpg'
            }
        ]

        album.save()
        resp = self.client.get(r('magicalbum:api'))
        resp = json.loads(resp.content)
        self.assertEqual(resp, album.pictures)
