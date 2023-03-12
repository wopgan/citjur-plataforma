from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from citjur.views import QuestionViewSet, AnswerViewSet
from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
