from django.urls import path
from . import views

#app_name = "polls"

urlpatterns = [

    

    path('LatestVersionView/', views.LatestVersionView.as_view(), name='LatestVersionView'),
    
    path('AddWatejaWoteView/', views.AddWatejaWoteView.as_view(), name='AddWatejaWoteView'),
    path('GetAllWatejaWoteView/', views.GetAllWatejaWoteView.as_view(), name='GetAllWatejaWoteView'),

    path('WatejaWoteCart/', views.WatejaWoteCartView.as_view(), name='WatejaWoteCart'),
    #path('WatejaWoteOrder/', views.WatejaWoteOrderView.as_view(), name='WatejaWote--order-list'),

]
