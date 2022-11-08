from rest_framework import serializers
from simulation_experiment.models import Simulexp_Model, SimulOutput_Model

class Simulexp_ModelSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    simulation_engine = serializers.StringRelatedField(read_only=True)
    simulation_code = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Simulexp_Model
        fields = "__all__"

class SimulOutput_ModelSerializer(serializers.ModelSerializer):

    simulation_exp = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SimulOutput_Model
        exclude = ["id"]





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
