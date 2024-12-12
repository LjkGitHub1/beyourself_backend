from django.urls import path
from rest_framework import routers
from zope.interface import named

from dvadmin.evaluate.views.scale import ScaleViewSet, QuestionViewSet, OptionViewSet, ScaleDataAPIView, ResultViewSet

system_url = routers.SimpleRouter()
system_url.register(r'scale', ScaleViewSet)

urlpatterns = [
    path('scale/', ScaleViewSet.as_view({'get': 'list','post': 'create'})),
    # path('scale/data/<int:scale_id>/', ScaleDataAPIView.as_view({'get':'list'}),name='scale_data'),
    path('scale/question/', QuestionViewSet.as_view({'get':'list','post':'create'})),
    path('scale/question/<int:pk>/', QuestionViewSet.as_view({'delete':'destroy','put':'update'})),
    path('scale/option/', OptionViewSet.as_view({'get':'list','post':'create'})),
    path('scale/option/<int:pk>/', OptionViewSet.as_view({'delete':'destroy','put':'update'})),
    path('scale/result/', ResultViewSet.as_view({'get':'list','post':'create'})),
    path('scale/result/<int:pk>/', ResultViewSet.as_view({'delete':'destroy','put':'update'})),
    # path('scale/question/', QuestionViewSet.as_view({'get': 'list','post': 'create'})),
]
urlpatterns += system_url.urls
