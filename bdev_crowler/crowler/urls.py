from django.urls import path
from .views import crawler_free_images, crawl_through_request

urlpatterns = [
    path("1/<str:search>", crawler_free_images, name='colect-data'),
    path("2/<str:search>", crawl_through_request, name='colect-data-request'),
]