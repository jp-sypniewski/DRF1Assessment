from django.urls import path
from JobBoard.api.views import JobOfferListCreateAPIView, JobOfferDetailAPIView

urlpatterns = [
    path("joboffers/", JobOfferListCreateAPIView.as_view() , name='job-offer-list'),
    path("joboffers/<int:pk>", JobOfferDetailAPIView.as_view() , name='job-offer-detail'),
]