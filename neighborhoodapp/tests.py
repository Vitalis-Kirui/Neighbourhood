import datetime
from .models import Business, Neighbourhood, Post, Profile 
from django.contrib.auth.models import User
from django.test import TestCase

class ProfileTest(TestCase):
    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighbourhood =  Neighbourhood(neighbourhood_name = "Sambu75", neighbourhood_location= "F-Society N", admin = self.user,neighbourhood_description='Home is best all the time', neighbourhood_photo="neighbourhood75.jpg")
        self.neighbourhood.save()
        self.profile = Profile(id=75,id_no=34931235,email='testingemail@g.com', profile_pic='profile.jpg', bio='Just testing profile class',neighbourhood=self.neighbourhood,
                                    user=self.user)
      
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        testsaved = Profile.objects.all()
        self.assertFalse(len(testsaved) < 0)    

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)

class NeighbourhoodTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighbourhood =  Neighbourhood(neighbourhood_name = "Sambu75", neighbourhood_location= "F-Society N", admin = self.user,neighbourhood_description='Home is best all the time', neighbourhood_photo="neighbourhood75.jpg")
        self.neighbourhood.save()
   
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save_neighbourhood(self):
        self.neighbourhood.save_hood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_neighbourhood(self):
        self.neighbourhood.delete_hood()
        testsaved = Neighbourhood.objects.all()
        self.assertFalse(len(testsaved) > 0)

class BusinessTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighbourhood =  Neighbourhood(neighbourhood_name = "Sambu75", neighbourhood_location= "F-Society N", admin = self.user,neighbourhood_description='Home is best all the time', neighbourhood_photo="neighbourhood75.jpg")
        self.neighbourhood.save()
        self.bussiness = Business(user=self.user,business_name="Business", business_neighbourhood=self.neighbourhood,business_email="business@gmail.com", business_description="Business setup")
        self.bussiness.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.bussiness,Business))

    def test_save_business(self):
        self.bussiness.save_business()
        bussiness = Business.objects.all()
        self.assertTrue(len(bussiness) > 0)

    def test_delete_hood(self):
        self.bussiness.delete_business()
        bussiness = Business.objects.all()
        self.assertFalse(len(bussiness) > 0)

