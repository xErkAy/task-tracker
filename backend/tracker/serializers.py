from rest_framework import serializers

from account.models import User
from project.utils import atomic_transaction
from tracker.models import Task, Tag
from tracker.services.task_handler import TaskHandler


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    full_name = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'full_name')


class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = UserSerializer()
    performer = UserSerializer()

    @atomic_transaction(message='Произошла ошибка при создании задачи')
    def create(self, validated_data):
        return TaskHandler.create(validated_data)

    @atomic_transaction(message='Произошла ошибка при обновлении задачи')
    def update(self, instance, validated_data):
        return TaskHandler.update(instance, validated_data)

    class Meta:
        model = Task
        fields = '__all__'
