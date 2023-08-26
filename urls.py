# urls.py
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... other paths ...
    path('complain', views.complain, name='complain'),
    path('hospital_portal/<str:name>/<str:aadhaar_number>/<str:pincode>/<str:mobile_number>/<str:severity>/<str:report_image>', views.hospital_portal, name='hospital_portal'),
    # ... other paths ...
]

# Serve uploaded media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
