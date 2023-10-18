from django.urls import path

from .models import Advertisement
from .views import IndexView, AdvertisementCreate, AdvertisementView, advertisement_detail


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', AdvertisementCreate.as_view(), name='create'),
    path('ju/', AdvertisementView.as_view(queryset=Advertisement.objects.filter(category__id=1)), name='post_list'),
    path('buy/', AdvertisementView.as_view(queryset=Advertisement.objects.filter(category__id=2)), name='post_list'),
    path('free/', AdvertisementView.as_view(queryset=Advertisement.objects.filter(category__id=3)), name='post_list'),
    path('sell/', AdvertisementView.as_view(queryset=Advertisement.objects.filter(category__id=4)), name='post_list'),
    path('services/', AdvertisementView.as_view(queryset=Advertisement.objects.filter(category__id=5)), name='post_list'),
    path('buy/<int:post_id>', advertisement_detail, name='post'),
    path('sell/<int:post_id>', advertisement_detail, name='post'),
    path('free/<int:post_id>', advertisement_detail, name='post'),
    path('services/<int:post_id>', advertisement_detail, name='post'),
    path('ju/<int:post_id>', advertisement_detail, name='post'),
]