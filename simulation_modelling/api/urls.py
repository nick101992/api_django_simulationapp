from django.urls import path
from simulation_modelling.api.views import (Simulation_ModelListCreateAPIView,
                                        Simulation_ModelDetailAPIView)


urlpatterns = [
    path("simulation_model/",
         Simulation_ModelListCreateAPIView.as_view(),
         name="simulation_model-list"),

    path("simulation_model/<int:pk>/",
         Simulation_ModelDetailAPIView.as_view(),
         name="simulation_model-detail"),

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
