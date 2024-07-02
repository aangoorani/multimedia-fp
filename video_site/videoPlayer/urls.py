from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('submit-comment/<str:uri>', views.submit_comment, name='submit_comment'),
    # path('get-summary', views.extra),
    path('<str:uri>/', views.show, name='video_page'),
]
