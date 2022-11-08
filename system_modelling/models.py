from django.db import models
from django.contrib.auth.models import User

class Model_Type(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class System_Model(models.Model):
    name = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    model_type = models.ForeignKey(Model_Type,
                                   on_delete=models.CASCADE,
                                   related_name="models_type")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name









# class Ebook(models.Model):
#     title = models.CharField(max_length=140)
#     author = models.CharField(max_length=60)
#     description = models.TextField()
#     publication_date = models.DateField()
#
#     def __str__(self):
#         return self.title
#
#
# class Review(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
#                                                      MaxValueValidator(5)])
#     review = models.TextField(blank=True, null=True)
#     review_author = models.ForeignKey(User, on_delete=models.CASCADE)
#     ebook = models.ForeignKey(Ebook,
#                               on_delete=models.CASCADE,
#                               related_name="reviews")
#
#     def __str__(self):
#         return str(self.rating)
