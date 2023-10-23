from django.urls import path
from app import views
urlpatterns = [
    path('',views.index),
    path('registration/',views.registration),
    path('table/' ,views.table),
    path('delete/<int:pk>/',views.delete),
    path('update/<int:uid>/',views.update,name='update'),
    path('update_view/',views.update_view),
    path('login/',views.login),
    path('login_view/',views.login_view)
]
