from django.urls import path
from . import views


urlpatterns = [
    #sets url path to home page
    path('', views.home, name="index"),
    #sets url path to createnewaccount
    path('create/', views.create_account, name='create'),
    #sets url path to balanceshet
    path('<int:pk>/balance/', views.balance, name='balance'),
    #sets url path to addnewtransaction
    path('transaction/', views.transaction, name='transaction')
]
