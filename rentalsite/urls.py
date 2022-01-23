from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'),namespace='home')),
    path('akun/', include(('akun.urls', 'akun'),namespace='akun')),
    path("booking/", include(('booking.urls', 'booking'), namespace="booking")),
    path('mobil/', include(('mobil.urls', 'mobil'),namespace='mobil')),
    path('motor/', include(('motor.urls', 'motor'),namespace='motor')),
]

#ADMIN TITLE
admin.site.site_header = "HALAMAN ADMIN - WEB RENTAL 2M"
admin.site.site_title = "ADMIN Page - 2M"
admin.site.index_title = "Selamat datang di halaman admin web rental 2M ..."
