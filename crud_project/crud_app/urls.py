
from django.urls import path
from.import views

urlpatterns = [
    path('',views.Add,name='Add'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:task_id1>/',views.update,name='update')
]
    
    