
from django.test import TestCase
from budget.models import Project, Expense, Category

class TestModels(TestCase):

    def setUp(self):
        self.desktopapp = Project.objects.create(
            name = "Desktop App",
            budget = 10000
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEquals(self.desktopapp.slug, 'desktop-app')

    def test_budget_left(self):

        category1 = Category.objects.create(
            project=self.desktopapp,
            name ='development'
        )

        Expense.objects.create (
            project=self.desktopapp,
            title='expense1',
            amount=1000,
            category=category1
        )

        Expense.objects.create (
            project=self.desktopapp,
            title='expense2',
            amount=2000,
            category=category1
        )

        self.assertEquals(self.desktopapp.budget_left, 7000)

    def test_project_total_transactions(self):

        project2 = Project.objects.create (
            name = 'project2',
            budget = 10000
        )

        category1 = Category.objects.create(
            project = self.desktopapp,
            name = 'development'
        )

        Expense.objects.create (
            project = self.desktopapp,
            title = 'expense1',
            amount = 1000,
            category = category1
        )
        Expense.objects.create (
            project = self.desktopapp,
            title = 'expense2',
            amount = 2000,
            category = category1
        )

        self.assertEquals(self.desktopapp.total_transactions, 2)
