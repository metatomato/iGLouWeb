from django.test import TestCase

class NavBarTest(TestCase):
    
    def test_can_self_render_template(self):
        response = self.client.get('/navbar/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'jumbotron.html')
        self.assertContains(response, '<title>navbar</title>')
