from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path('', views.check_in, name = "check_in"),
    path('index', views.logincheck),
    path('view_map/', views.view_map, name='view_map'),
    path('viewusers/', views.viewusers, name='viewusers'),
    path('sign_in/', views.signpost, name="sign_in"),
    path('logout', views.logout_view, name="logout"),
    path('forgot_password', views.forgotpass, name="forgot_password")
]
=======
    path('', views.index),
    path('check_in/', views.check_in, name='check_in'),
    path('viewusers/', views.viewusers, name='viewusers'),
    path('sign_in/', views.signpost, name="sign_in"),
    path('check_in/check', views.logincheck)
]



# path('view_map/', views.view_map, name='view_map'),
    # path('view_map/check_in/', views.view_map.check_in, name='check_in1'),

>>>>>>> cd7c48fda2d9c8f31b8f9b76aa2c63c8867ea2d9
=======
    path('', views.check_in, name="checkin"),
    path('check', views.logincheck),
    path('view_map/', views.view_map, name='view_map'),
    path('sign_in/', views.signpost, name="sign_in"),
    path('logout', views.logout_view, name="logout"),
    path('index', views.index, name="index"),
    path('forgotpassword', views.forgotpassword, name="forgotpassword"),
    path('forgotpassword/emailsend', views.sendEmail, name="emailsend"),
    path('changepassword', views.changepass, name="changepass"),
    path('changepassword/change', views.changePassword),
    path('view_map', views.updateOccupancy, name="update"),
]
>>>>>>> featuresandlogin
