from django.urls import path
from simulation_experiment.api.views import (Simulexp_ModelListCreateAPIView,
                                             Simulexp_ModelDetailAPIView,
                                             SimulOutput_ModelListCreateAPIView)


urlpatterns = [
    path("simul_exp/",
         Simulexp_ModelListCreateAPIView.as_view(),
         name=" Simulexp-list"),

    path("simul_exp/<int:pk>/",
         Simulexp_ModelDetailAPIView.as_view(),
         name=" Simulexp-detail"),

    path("simul_exp/<int:simulexp_pk>/outputs/",
         SimulOutput_ModelListCreateAPIView.as_view(),
         name=" Simulexp-detail"),

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
