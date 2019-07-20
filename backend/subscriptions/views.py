from .models import Subscription
from .serializers import SubscriptionSerializer
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import generics
from django.shortcuts import render
from django.views.decorators.cache import cache_page

class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @cache_page(CACHE_TTL)
# def recipes_view(request):
#     return render(request, 'cookbook/recipes.html', {
#         'recipes': get_recipes()
#     })