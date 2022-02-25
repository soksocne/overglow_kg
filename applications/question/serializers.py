from rest_framework import serializers

from applications.question.models import Category, Question, Answer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'question', 'solution', 'image')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        answer = Answer.objects.create(**validated_data)
        return answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'category', 'title', 'image', 'problem')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        question = Question.objects.create(**validated_data)
        return question

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.title
        rep['author'] = instance.author.email
        rep['solutions'] = AnswerSerializer(Answer.objects.filter(question=instance.id), many=True).data
        return rep
