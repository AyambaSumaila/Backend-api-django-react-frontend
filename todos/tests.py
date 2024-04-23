from django.test import TestCase
from .models import Todo 

# Create your tests here.
class TodoModelTest(TestCase):
    @classmethod 

    #Setup data to be tested against 
    def setUpTestData(cls):
        Todo.objects.create(title="Test First title", body="Test First body")

    #Test method for the title
    def test_title_content(self):
        todo=Todo.objects.get(id=1)
        expected_object_name=f'{todo.title}'
        self.assertEqual(expected_object_name, 'Test First title')

    #Test method for the body 
    def test_body_content(self):
        todo=Todo.objects.get(id=1)
        expected_object_name=f'{todo.body}'
        self.assertEqual(expected_object_name, 'Test First body')