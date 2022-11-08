from django.urls import path
from system_modelling.api.views import (System_ModelListCreateAPIView,
                                        System_ModelDetailAPIView)


urlpatterns = [
    path("system_model/",
         System_ModelListCreateAPIView.as_view(),
         name="system_model-list"),

    path("system_model/<int:pk>/",
         System_ModelDetailAPIView.as_view(),
         name="system_model-detail"),

]



# urlpatterns = [
#     path("ebooks/",
#          EbookListCreateAPIView.as_view(),
#          name="ebook-list"),
#
#     path("ebooks/<int:pk>/",
#          EbookDetailAPIView.as_view(),
#          name="ebook-detail"),
#
#     path("ebooks/<int:ebook_pk>/review/",
#          ReviewCreateAPIView.as_view(),
#          name="review-ebook"),
#
#     path("reviews/<int:pk>/",
#          ReviewDetailAPIView.as_view(),
#          name="review-detail")
# ]
