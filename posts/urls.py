from django.urls import path
from rest_framework.routers import SimpleRouter

# Using viewsets
from .views import UserViewSet, PostViewSet

# Using indidivual views for each endpoint
# from .views import PostLIst, PostDetail, UserList, UserDetail

# Using viewsets
router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls


# Using individual endpoints
# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]