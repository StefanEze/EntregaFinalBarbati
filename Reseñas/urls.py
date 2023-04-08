from django.urls import path
from Reseñas import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('home', views.inicio, name="Inicio"),
    path('biografia', views.biografia, name="Biografia"),
    path('form_review/',views.reviews,name="Reviews"),
    path("list",views.list,name="List"),
    path('detalle/<str:pk>',views.detalle,name="Detail"),
    path('update-review/<str:pk>',views.updateReview, name="Edit"),
    path('delete-review/<str:pk>/',views.deleteReview,name="Delete"),
]