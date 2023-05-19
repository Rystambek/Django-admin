from django.urls import path
from api.views import home,smartphones,add_smartphone,get_id,get_delete,get_update

urlpatterns = [
    path('', home),
    path('get/all/',smartphones),
    path('add/',add_smartphone),
    path('get/<int:id>',get_id),
    path('delete/<int:id>',get_delete),
    path('update/<int:id>',get_update)
]
