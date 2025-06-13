from .import views
from django.urls import include, path
urlpatterns=[
    path('',views.index, name='index'),
    path('welcome',views.welcome,name='welcome'),
    path('<int:expense_id>', views.detail, name='detail'),
    path('delete/<int:expense_id>', views.delete_item, name='delete_item'),
    path('addItem', views.add_item, name='add_item'),
    path('updateItem/<int:expense_id>', views.update_item, name='update_item'),
    path('pdf/', views.pdf, name='pdf'),
    
]