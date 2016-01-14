from django.test import TestCase
from . import models
from django.contrib.auth import get_user_model

# Create your tests here.

class TestProfileModel(TestCase):
    
    def test_profile_creation(self):
        User = get_user_model()
        # New user created
        user = User.objects.create(username="testuser",
                                   password="123")
        
        # Check that a Profile instance has been created
        self.assertIsInstance(user.profile, models.Profile)
        # Call save method to activate signal again, and ensure
        # that is does not create another profile instance
        user.save()
        self.assertIsInstance(user.profile, models.Profile)
        
class TestSubjectModel(TestCase):
    
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username="testuser",
                                        password="123")
        self.profile = self.user.profile
        
    def tearDown(self):
        self.user.delete()
    
    def test_name(self):
        subject = models.Subject(user=self.profile,
                                 name="Science")
        self.assertTrue(subject.name == "Science")