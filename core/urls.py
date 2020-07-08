from django.urls import include

from rest_framework import routers

from core.api import BookViewSet, BookListViewSet, PersonViewSet

router = routers.DefaultRouter()

router.register(r'book', BookViewSet)
router.register(r'booklist', BookListViewSet)
router.register(r'person', PersonViewSet)

urlpatterns = router.urls