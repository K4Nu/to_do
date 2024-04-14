from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
import datetime

class TaskModelTestCase(TestCase):

    def setUp(self):
        # Create a user for the foreign key requirement
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_create_task(self):
        # Creating a Task instance
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            content='Task content here',
            color='#FFFFFF',  # Assuming this is a valid color code for the task
        )

        # Check if the task is created with correct title and content
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.content, 'Task content here')

        # Check the default date fields
        self.assertEqual(task.date_start, datetime.date.today())
        self.assertEqual(task.date_end, datetime.date.today())

        # Check the default status
        self.assertTrue(task.status)

        # Check the string representation of the task
        self.assertEqual(str(task), 'Test Task')


