from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from simulation_modelling.models import Simulation_Type, Simulation_Model
from simulation_modelling.api.serializers import Simulation_ModelSerializer
from simulation_modelling.api.permissions import IsModelAuthor
from simulation_modelling.api.pagination import SmallSetPagination

class Simulation_ModelListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = Simulation_ModelSerializer
    permission_classes = [IsModelAuthor]
    pagination_class = SmallSetPagination

    def get_queryset(self):
        author = self.request.user
        if author.is_authenticated:
         author_queryset = Simulation_Model.objects.filter(author=author).order_by("id")
         return author_queryset
        return Simulation_Model.objects.none()


class Simulation_ModelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Simulation_Model.objects.all()
    serializer_class = Simulation_ModelSerializer
    permission_classes = [IsModelAuthor]


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
