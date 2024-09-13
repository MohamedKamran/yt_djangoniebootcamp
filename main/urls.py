from django.urls import path
from .views import YoutuberListView, YoutuberDetailView, YoutuberCreateView, YoutuberUpdateView, YoutuberDeleteView

urlpatterns = [
    path('', YoutuberListView.as_view(), name='youtuber_list'),
    path('youtuber/<int:pk>/', YoutuberDetailView.as_view(), name='youtuber_detail'),
    path('youtuber/new/', YoutuberCreateView.as_view(), name='youtuber_new'),
    path('youtuber/<int:pk>/edit/', YoutuberUpdateView.as_view(), name='youtuber_edit'),
    path('youtuber/<int:pk>/delete/', YoutuberDeleteView.as_view(), name='youtuber_delete'),
]