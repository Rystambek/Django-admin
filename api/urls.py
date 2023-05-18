from django.urls import path
from api.views import home,smartphones

urlpatterns = [
    path('', home),
    path('smartphone/',smartphones)
]
