""" Module for Magic Album tests """

from django.test import TestCase
from django.core.urlresolvers import reverse as r


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
