from django.urls import path

from task_manager.statuses import views

urlpatterns = [
    path('', views.ListStatuses.as_view(), name='statuses_list'),
    path('create/', views.AddStatus.as_view(), name='add_status'),
    path('<int:pk>/update/', views.UpdateStatus.as_view(),
         name='update_status'),
    path('<int:pk>/delete/', views.DeleteStatus.as_view(),
         name='delete_status'),
]
