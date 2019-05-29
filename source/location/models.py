from django.db import models
from django.contrib.auth.models import Permission
from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404
from datetime import datetime
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class userlocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curloc = models.TextField(null=True,blank=True)
    radius = models.IntegerField(null=True,blank=True)
    days = models.IntegerField(null=True,blank=True)
    budget= models.IntegerField(null=True,blank=True)
    r_list=((1,'Church'),(2,'Gurudwara'),(3,'Hindu Temple'),(4,'Jain Temple'),(5,'Monestary'),(6,'Mosque'),(7,"Buddhist Pilgrimage"),(8,"Hindu Pilgrimage"),(9,"Sikh Pilgrimage"),(10,"Historical Place"),(11,"Palace"),(12,"Fort"),(13,"Cave"),(14,"Architecture"),(15,"Monument"),(16,"Museum"),(17,"Desert"),(18,"Coast"),(19,"Port"),(20,"Beach"),(21,"Island"),(22,"River Bank"),(23,"Dam"),(24,"Lake"),(25,"Backwaters"),(26,"Waterfalls"),(27,"Forest"),(28,"Garden"),(29,"Zoo"),(30,"National Park"),(31,"Bird Sanctuary"),(32,"Wildlife Sanctuary"),(33,"Hills"),(34,"Valley"),(35,"Snow"),(36,"Hill Station"),(37,"Tea Estate"),(38,"City"),(39,"Market"),(40,"Park"),(41,"Food"),(0,'None'))

    reason1 = models.IntegerField(choices=r_list, blank=True,null=True)
    reason2 = models.IntegerField(choices=r_list, blank=True,null=True)
    reason3 = models.IntegerField(choices=r_list, blank=True,null=True)
    reason4 = models.IntegerField(choices=r_list, blank=True,null=True)
    reason5 = models.IntegerField(choices=r_list, blank=True,null=True)
    reason6 = models.IntegerField(choices=r_list, blank=True,null=True)
    reason7 = models.IntegerField(choices=r_list, blank=True,null=True)
    reason8 = models.IntegerField(choices=r_list, blank=True,null=True)   