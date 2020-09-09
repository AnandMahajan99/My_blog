from django.urls import path
from blog import views

# all urls come here

urlpatterns = [

    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:id>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:id>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/draft/', views.DraftListView.as_view(), name='post_draft_view'),

    path('about/', views.AboutView.as_view(), name='about'),
]