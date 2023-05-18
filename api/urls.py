from django.urls import path
from api.views import home,smartphones,add_smartphone,get_id,get_delete

urlpatterns = [
    path('', home),
    path('get/all/',smartphones),
    path('add/',add_smartphone),
    path('get/<id>',get_id),
    path('delete/<id>',get_delete)
]
