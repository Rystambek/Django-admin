from django.urls import path
from api.views import home,smartphones,add_smartphone

urlpatterns = [
    path('', home),
    path('smartphone/',smartphones),
    path('add/',add_smartphone)
]
