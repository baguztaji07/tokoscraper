from django.urls import path
from . import views

urlpatterns = [
    path('tokopedia/', views.tokopedia, name='tokopedia'),
    path('bukalapak/', views.bukalapak, name='bukalapak'),
    path('tokopedia/download/', views.tokopedia_download, name='tokopedia_download'),
    path('bukalapak/download/', views.bukalapak_download, name='bukalapak_download'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('update/<int:id>', views.update, name='update'),
    # path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]