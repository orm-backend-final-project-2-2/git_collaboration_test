from django.test import TestCase

class PostListTestCase(TestCase):

    def test_always_success(self):
        self.assertEqual(True, True)
        
class IntergrationTestCase(TestCase):
    def test_always_success(self):
        self.assertEqual(True, True)