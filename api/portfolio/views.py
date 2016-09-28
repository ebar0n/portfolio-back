from rest_framework import filters, viewsets

from portfolio import models, serializers


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Tag
    """
    filter_backends = (filters.SearchFilter,)
    pagination_class = None
    queryset = models.Tag.objects.all()
    search_fields = ('name',)
    serializer_class = serializers.TagSerializer


class DeveloperViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Developer
    """
    filter_backends = (filters.SearchFilter,)
    queryset = models.Developer.objects.filter(user__is_active=True)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')
    serializer_class = serializers.DeveloperSerializer


class EntryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Entry
    """
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('developer', 'tags')
    queryset = models.Entry.objects.filter(developer__user__is_active=True)
    search_fields = ('title',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.EntryRetrieveSerializer
        return serializers.EntrySerializer
