from rest_framework import routers
from geoHub.viewsets import ArticleViewSet

router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)