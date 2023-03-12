from .models import Questions, Answer
from .serializers import QuestionsSerializer, AnswerSerializer
from rest_framework import viewsets


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

