from django.urls import path
from . import views

app_name = 'editor'

urlpatterns = [
    path('query/', views.query_form, name='query_form'),
    path('queries/', views.query_list, name='query_list'),
]
app_name = 'snippets'

urlpatterns = [
    path('', views.code_snippet_list, name='snippet_list'),
    path('create/', views.code_snippet_create, name='snippet_create'),
    path('<int:snippet_id>/', views.code_snippet_detail, name='snippet_detail'),
    path('<int:snippet_id>/edit/', views.code_snippet_edit, name='snippet_edit'),
    path('<int:snippet_id>/delete/', views.code_snippet_delete, name='snippet_delete'),
]
