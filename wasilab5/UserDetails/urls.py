from django.urls import path
from . import views

urlpatterns = [
        path('', views.UploadDataView, name='UploadDataView'),
        path('dns', views.UploadData, name='UploadData'),
        path('dns-cart', views.UploadDnsInformation, name='UploadDnsInformation'),
        path('dns-buy', views.DnsIcann, name='DnsIcann'),
        path('wasi-congratulations/<str:args>/', views.DnsCongratulations, name='DnsCongratulations')
]