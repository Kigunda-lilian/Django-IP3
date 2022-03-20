from django.contrib.auth.models import User
from django.test import TestCase
from .models import Project

# Create your tests here.


class ProjectTestClass(TestCase):  # Project class test
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="Nashlil", first_name="Lilian", last_name="Kanana"
        )

        self.project = Project(
            title="Project Test",
            description="Project  Description",
            image="image.jpg",
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.project.save_project()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)




