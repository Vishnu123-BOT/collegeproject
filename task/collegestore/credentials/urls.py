from django.urls import path
from. import views
app_name='credentials'
urlpatterns = [


  path('register', views.register, name='register'),
  path('login',views.login,name='login'),
  path('new',views.new,name='new'),
  path('add/',views.student_create,name='student_add'),
  path('get_courses',views.get_courses,name='get_courses'),
  path('<int:pk>/',views.student_update,name='student_change')
]