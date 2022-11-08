from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from system_modelling.models import Model_Type, System_Model
from system_modelling.api.serializers import System_ModelSerializer
from system_modelling.api.permissions import IsModelAuthor
from system_modelling.api.pagination import SmallSetPagination

class System_ModelListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = System_ModelSerializer
    permission_classes = [IsModelAuthor]
    pagination_class = SmallSetPagination

    def get_queryset(self):
        author = self.request.user
        if author.is_authenticated:
         author_queryset = System_Model.objects.filter(author=author).order_by("id")
         return author_queryset
        return System_Model.objects.none()


class System_ModelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = System_Model.objects.all()
    serializer_class = System_ModelSerializer
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
