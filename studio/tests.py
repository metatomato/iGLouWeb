from django.test import TestCase

class StudioTest(TestCase):
    
    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'base.html')

