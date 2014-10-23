from django.test import TestCase

# Create your tests here.
class NewsTest(TestCase):

    def test_can_self_render_template(self):
        response = self.client.get('/news/')
        self.assertTemplateUsed(response, 'news.html')
        self.assertContains(response,'<title>news</title>')