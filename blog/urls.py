#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Hazycrown
#
# Created:     14/09/2019
# Copyright:   (c) Hazycrown 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [path('', views.post_list, name='post_list'),]