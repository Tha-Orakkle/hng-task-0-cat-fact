from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from base.views import UserCatDataView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='spectacular-doc'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='spectacular-doc'),
    path('me', UserCatDataView.as_view(), name='data-view')
]
