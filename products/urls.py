from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tokopedia/', views.tokopedia, name='tokopedia'),
    path('bukalapak/', views.bukalapak, name='bukalapak'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('update/<int:id>', views.update, name='update'),
    # path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]