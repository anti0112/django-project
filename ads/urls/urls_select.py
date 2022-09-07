from ads.views import *
from django.urls import path

urlpatterns = [
    path("", SelectionListView.as_view(), name="home"),
    path("<int:pk>/", SelectionDetailView.as_view(), name="get_pk"),
    path("create/", SelectionCreateView.as_view(), name="create"),
    path("<int:pk>/update/", SelectionUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", SelectionDeleteView.as_view(), name="delete"),
    
]