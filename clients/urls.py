from django.urls import path
from .views import *

app_name = 'clients'

urlpatterns = [
    path("", ClientListView.as_view(), name='client_list'),
    path("create", ClientCreateView.as_view(), name='client_create'),
    path("<int:client_id>", client_detail, name='client_detail'),
    path("<int:pk>/update", ClientUpdateView.as_view(), name='client_update'),
    path("<int:client_id>/delete", client_delete, name='client_delete'),
    path('<int:client_id>/visits/create', client_visit_create, name='client_visit_create'),
    path('visits/<int:visit_id>', visit_detail, name='visit_detail'),
    path('visits/<int:visit_id>/update', visit_update, name='visit_update'),
    path('visits', VisitListView.as_view(), name='visit_list'),
    path('visits/create', visit_create, name='visit_create'),
    path("search", ClientSearchView.as_view(), name='client_search'),
]