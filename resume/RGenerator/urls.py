from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('info_form/', views.UseCVForm.as_view(), name='info_form'),
    path('pattern_resume/', views.resume_pattern, name='resume_pattern'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('download/', views.download, name='download'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)