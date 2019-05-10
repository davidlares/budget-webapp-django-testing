from django.test import TestCase, Client
from django.urls import reverse
from budget.models import Project, Category, Expense
import json

class TestViews(TestCase):

    # runs before any test here
    def setUp(self):
        self.client = Client() # creating a client
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['desktop-app'])
        # creating a object for getting the slug correctly (override  save method)
        self.desktopapp = Project.objects.create(
            name = "Desktop app",
            budget = 10000
        )

    # GET methods

    def test_project_list_get(self):
        response = self.client.get(self.list_url) # setting up the client
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_project_detail_get(self):
        response = self.client.get(self.detail_url) # setting up the client
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')

    # POST methods

    def test_project_detail_POST_new_expense(self):

        Category.objects.create (
            project = self.desktopapp,
            name = 'development'
        )

        response = self.client.post(self.detail_url, {
            'title': 'expense1',
            'amount': 1000,
            'category': 'development'
        })

        # because the view redirection
        self.assertEquals(response.status_code, 302)
        # getting the project
        self.assertEquals(self.desktopapp.expenses.first().title, 'expense1')

    #empty
    def test_project_detail_post_no_data(self):

        response = self.client.post(self.detail_url)
        # because the view redirection
        self.assertEquals(response.status_code, 302)
        # getting the project
        self.assertEquals(self.desktopapp.expenses.count(), 0)

    # DELETE methods

    def test_project_detail_delete_expense(self):

        category1 = Category.objects.create (
            project = self.desktopapp,
            name = 'development'
        )

        Expense.objects.create(
            project = self.desktopapp,
            title = 'expense1',
            amount = 1000,
            category = category1
        )

        response = self.client.delete(self.detail_url, json.dumps({
            'id': 1
            # the created expense ID
        }))
        # intensional broken = should be 302
        self.assertEquals(response.status_code, 204)
        self.assertEquals(self.desktopapp.expenses.count(), 0)
