from django.test import LiveServerTestCase
from selenium import webdriver

class IndexTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_has_proper_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn('RDG', self.browser.title)
