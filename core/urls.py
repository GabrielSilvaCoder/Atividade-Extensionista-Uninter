from django.contrib import admin
from django.urls import path, include
from help_enchentes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_view, name='home'),
    path('category/<tag>', home_view, name='category'),
    path('report/create/', report_create_view, name='report-create'),
    path('report/delete/<pk>', report_delete_view, name='report-delete'),
    path('report/edit/<pk>', report_edit_view, name='report-edit'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
