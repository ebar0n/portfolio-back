from rest_framework import filters, mixins, viewsets

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


class DeveloperViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for Developer
    """
    pagination_class = None
    serializer_class = serializers.DeveloperSerializer

    def get_queryset(self):
        return models.Developer.objects.filter(
            user__is_active=True,
            domain=self.request.META.get('HTTP_HOST', '')
        )


class EntryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Entry
    """
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('tags',)
    queryset = models.Entry.objects.filter(developer__user__is_active=True)
    search_fields = ('title',)

    def get_queryset(self):
        return models.Entry.objects.filter(
            developer__user__is_active=True,
            developer__domain=self.request.META.get('HTTP_HOST', '')
        )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.EntryRetrieveSerializer
        return serializers.EntrySerializer
