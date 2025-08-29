from rest_framework import mixins, viewsets


class CreateRetrieveDestroyMixin(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    """
    Миксин для создания удаления и получения объекта
    """
    pass

class CreateListRetrieveDestroyMixin(
    CreateRetrieveDestroyMixin,
    mixins.ListModelMixin
):
    """
    Миксин для создания, удаление, получение объекта и списка объектов
    """
    pass
