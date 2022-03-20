from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        """creation of profile for testing
        """
        user = User.objects.create(
            username = 'nashlil',
            first_name = 'lilian',
            last_name = 'kanana')
        
        Profile.objects.create(
            bio = 'Back end developer',
            image = 'media/profile_pics/pizzacart10-removebg-preview_edhHkdQ.png',
            user_id = user.id
        )

    
    def test_bio(self):
        """tests the profiles bio
        """
        profile=Profile.objects.get(bio="Back end developer")
        self.assertEqual(profile.bio, "Back end developer")
        