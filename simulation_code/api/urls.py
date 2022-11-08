from django.urls import path
from simulation_code.api.views import (Codesimul_ModelListCreateAPIView,
                                       Codesimul_ModelDetailAPIView)


urlpatterns = [
    path("simulation_code/",
         Codesimul_ModelListCreateAPIView.as_view(),
         name="code_model-list"),

    path("simulation_code/<int:pk>/",
         Codesimul_ModelDetailAPIView.as_view(),
         name="code_model-detail"),

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
