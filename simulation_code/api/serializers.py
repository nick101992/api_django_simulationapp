from rest_framework import serializers
from simulation_code.models import Codesimul_Model

class Codesimul_ModelSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    simulation_model = serializers.StringRelatedField(read_only=True)
    codesimul_type = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Codesimul_Model
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
