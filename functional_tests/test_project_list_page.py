from selenium import webdriver
from budget.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        # chromedriver program location (MAC OS binary)
        self.browser = webdriver.Chrome('functional_tests/chromedriver') # fire up browser

    # runs after every test
    def tearDown(self):
        self.browser.close()

    def test_no_project_alert_is_displayed(self):
        self.browser.get(self.live_server_url) # locate to the server (StaticLiveServerTestCase)
        # first time request
        alert = self.browser.find_element_by_class_name('noproject-wrapper') # checking DOM element
        # conditioning test
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text, 'Sorry, you don\'t have any projects, yet.'
        )

    def test_no_projects_alert_button_redirects_to_add_page(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('add')
        # getting the a tag
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(self.browser.current_url, add_url)

    def test_user_sees_project_list(self):

        project = Project.objects.create(
            name ='project1',
            budget = 10000
        )

        self.browser.get(self.live_server_url)
        self.assertEquals(
            self.browser.find_element_by_tag_name('h5').text, 'project1'
        )
