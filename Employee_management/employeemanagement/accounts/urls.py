from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addemployee/',views.add_employee,name='add_employee'),
    path('allemployee/',views.all_employee,name='all_employee'),
    path('remove/<int:id>',views.remove_employee,name='delete'),
    path('edit/<int:id>',views.Edit_employee,name='edit'),
]
