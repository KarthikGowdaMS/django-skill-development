from django.urls import path
from . import views

from jobs.views import Forms, StudentList, StudentDetail, StudentUpdate, StudentDelete

urlpatterns = [
    # path("", views.home, name="index"),
    path('register/', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),
    path('students/', views.students , name = "students"),
    # path("register/", views.register, name="register"),
    # path("login/", views.login, name="login"),
    # path("dashboard/", views.template_view, name="dashboard"),
    # path("time/", views.time, name="time"),
    #create path for first_view, second_view, third_view, till fifth_view
    # path("first/", views.first_view, name="first_view"),
    # path("second/", views.second_view, name="second_view"),
    # path("third/", views.third_view, name="third_view"),
    # path("fourth/", views.fourth_view, name="fourth_view"),
    # path("fifth/", views.fifth_view, name="fifth_view"),
    # path('students', views.students , name = "students"),
    path('forms', Forms.as_view(), name = 'forms'),
    path('', StudentList.as_view(), name = 'list'),
    path('<pk>/detail', StudentDetail.as_view(), name = 'detail'),
    path('<pk>/update', StudentUpdate.as_view(), name = 'update'),
    path('<pk>/delete', StudentDelete.as_view(), name = 'delete'),
    path('index/', views.index , name = "index"),
    path('about/', views.about , name = "about"),
    path('blog/', views.blog , name = "blog"),
    path('contact/', views.contact , name = "contact"),
    path('portfolio/', views.portfolio , name = "portfolio"),


]
    
     

