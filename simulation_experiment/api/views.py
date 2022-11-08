from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from simulation_experiment.models import Simulexp_Model, SimulOutput_Model
from simulation_experiment.api.serializers import Simulexp_ModelSerializer, SimulOutput_ModelSerializer
from simulation_experiment.api.permissions import IsModelAuthor
from simulation_experiment.api.pagination import SmallSetPagination

class Simulexp_ModelListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = Simulexp_ModelSerializer
    permission_classes = [IsModelAuthor]
    pagination_class = SmallSetPagination

    def get_queryset(self):
        author = self.request.user
        if author.is_authenticated:
         author_queryset = Simulexp_Model.objects.filter(author=author).order_by("id")
         return author_queryset
        return Simulexp_Model.objects.none()

class Simulexp_ModelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Simulexp_Model.objects.all()
    serializer_class = Simulexp_ModelSerializer
    permission_classes = [IsModelAuthor]

class SimulOutput_ModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = SimulOutput_Model.objects.all()
    serializer_class = SimulOutput_ModelSerializer

    def get_queryset(self):
        simulexp_pk = self.kwargs.get("simulexp_pk")
        simulexp = get_object_or_404(Simulexp_Model, pk=simulexp_pk)
        simuloutput_queryset = SimulOutput_Model.objects.filter(simulation_exp=simulexp)
        return simuloutput_queryset




# class ReviewCreateAPIView(generics.CreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         ebook_pk = self.kwargs.get("ebook_pk")
#         ebook = get_object_or_404(Ebook, pk=ebook_pk)
#
#         review_author = self.request.user
#
#         review_queryset = Review.objects.filter(ebook=ebook,
#                                                 review_author=review_author)
#         if review_queryset.exists():
#             raise ValidationError("Hai già recensito questo ebook!")
#
#         serializer.save(ebook=ebook, review_author=review_author)
#
#
# class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [IsReviewAuthorOrReadOnly]
