from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView

# Inheritance class (SimpleTestCase) for working with the BD
class TestUrls(SimpleTestCase):

    # should all start with test_
    def test_list_url_is_resolved(self):
        url = reverse('list') # url name
        # print(resolve(url)) # the resolve object to validate the name of the resolving view
        self.assertEquals(resolve(url).func, project_list)

    def test_add_url_is_resolved(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView) # this is a class view

    def test_list_url_slug_is_resolved(self):
        url = reverse('detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, project_detail)
