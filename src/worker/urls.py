from django.urls import path

from . import views

urlpatterns = [
    path('employees/', views.EmployeeView.as_view({"get": "list", 'post': 'create'}), name='employees-list'),
    path('employees/<int:pk>/', views.EmployeeView.as_view({'delete': 'destroy'}), name='employees-detail'),
    path('departments/', views.DepartamentView.as_view({'get': 'list'}), name='departments')
]
