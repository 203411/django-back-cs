from django.urls import path, include, re_path

from Profile.views import ProfileTable

urlpatterns = [
    re_path(r'^profile',ProfileTable.as_view()),
    # re_path(r'^user/(?<id_user>d+)$',ProfileTableDetail.as_view()),
] 