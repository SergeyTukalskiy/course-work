from rest_framework import serializers
# from base.models import Item
from base.models import Item, Student

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class StepsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1, max_length=100)
    is_correct = serializers.BooleanField()

class StudentSerializer(serializers.ModelSerializer):
    steps = StepsSerializer(many=True)
    class Meta:
        model = Student
        fields = ('user_id', 'name', 'username', 'password', 'title',
                  'teacherName', 'teacherId', 'steps')
