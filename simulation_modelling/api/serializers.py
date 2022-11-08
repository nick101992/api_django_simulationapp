from rest_framework import serializers
from simulation_modelling.models import Simulation_Model

class Simulation_ModelSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    system_model = serializers.StringRelatedField(read_only=True)
    simulation_type = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Simulation_Model
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
