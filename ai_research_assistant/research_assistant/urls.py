from django.urls import path
from .views import ResearchPaperAnalysisView

urlpatterns = [
    path("analyze/", ResearchPaperAnalysisView.as_view(), name="analyze_paper"),
]
