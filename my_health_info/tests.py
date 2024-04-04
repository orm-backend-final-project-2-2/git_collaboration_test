from django.test import TestCase


# Create your tests here.
class DietTestCase(TestCase):
    def test_always_success(self):

        self.assertEqual(True, True)


class IntergrationTestCase(TestCase):
    def test_always_success(self):
        self.assertEqual(True, True)
