from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from stack_overflow_kg import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('question/', include('applications.question.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
