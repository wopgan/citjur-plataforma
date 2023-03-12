from rest_framework import serializers
from .models import Answer, Questions


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'resposta']


class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'pergunta', 'respondida']