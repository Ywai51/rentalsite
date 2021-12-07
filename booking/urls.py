from django.urls import path

from . import views

urlpatterns = [
    path('mobil/<slug:claimInput>/', views.mblBooking, name="mobil" ),
    path('motor/<slug:claimInput>/', views.mtrBooking, name="motor" ),
]