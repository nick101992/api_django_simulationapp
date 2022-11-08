from rest_framework import permissions


class IsModelAuthor(permissions.BasePermission):
    """ la visualizzazione, l'update e il delete aono concessi solo agli autori
    del modello del sistema """

    def has_object_permission(self, request, view, obj):

        return obj.author == request.user
