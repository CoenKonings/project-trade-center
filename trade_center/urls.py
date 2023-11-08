from django.urls import path
from .views import ProposalDetailView, CreateProposalView

urlpatterns = [
    path("", CreateProposalView.as_view(), name="create-proposal"),
    path("proposals/<int:pk>/", ProposalDetailView.as_view(), name="proposal-detail"),
]
