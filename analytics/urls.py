from django.urls import path

from analytics.views import analyticsAPIView

urlpatterns = [path("", analyticsAPIView.as_view())]
