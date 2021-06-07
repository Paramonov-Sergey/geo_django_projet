
from django.urls import path
from.views import *
app_name='measurements'

urlpatterns = [

    path('',CalculateView.as_view(),name='calculate_view'),
    path('<int:pk>/',CalculateView.as_view(),name='view_map'),
]
