
from django.urls import path
from. import views

app_name='collegestoreapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('alldepdetails/<int:pk>/',views.alldepdetails,name='alldepdetails')


]