from django.test import TestCase
from .models import TODO

# Create your tests here.
class TODOModelTest(TestCase):
    @classmethod
    def setUpTEstData(cls):
        TODO.objects.create(title='first todo')
        TODO.objects.create(description='a description here')

    
    def test_title_content(self):
        todo = TODO.object.get(id=1)
        expect_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')
    
    def test_description_content(self):
        todo = TODO.objects.get(id=2)
        excepted_object_name = f'{todo.description}'
        self.assertEquals(expected_object_name, 'a description here')