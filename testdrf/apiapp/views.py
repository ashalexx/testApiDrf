from rest_framework import generics, viewsets
from .serializers import *
from .models import *
from .permissions import IsOwnerOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ProductAccessViewSet(viewsets.ModelViewSet):
    queryset = ProductAccess.objects.all()
    serializer_class = ProductAccessSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonViewViewSet(viewsets.ModelViewSet):
    queryset = LessonView.objects.all()
    serializer_class = LessonViewSerializer
    filter_fields = ['user']

    def get_queryset(self):
        # Фильтрация только по текущему пользователю
        return self.queryset.filter(user=self.request.user)

    

