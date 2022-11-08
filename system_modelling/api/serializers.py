from rest_framework import serializers
from system_modelling.models import System_Model

class System_ModelSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    model_type = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = System_Model
        fields = "__all__"











# class ReviewSerializer(serializers.ModelSerializer):
#
#     review_author = serializers.StringRelatedField(read_only=True)
#
#     class Meta:
#         model = Review
#         # fields = "__all__"
#         exclude = ["ebook"] # passato automaticamente via perform_create
#
#
# class EbookSerializer(serializers.ModelSerializer):
#     reviews = ReviewSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Ebook
#         fields = "__all__"
