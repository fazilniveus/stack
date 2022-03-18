from django.urls import path
from .import views

app_name = 'datainfo'

urlpatterns = [
    path('',views.home, name='home'),

    #crud 
    path('questions/',views.QuestionListView.as_view(),name= 'question_list'),
   # path('questions/<int:pk>/',views.QuestionDetailView.as_view(), name = 'question_detail'),
]
