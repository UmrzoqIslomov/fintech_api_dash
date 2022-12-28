from rest_framework import serializers

from apps.courses.models.courses import CourseModel


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.image = validated_data.get("image")
        instance.teacher = validated_data.get("teacher")
        instance.course = validated_data.get("course")
        instance.price = validated_data.get("price")
        instance.lessons_amount = validated_data.get("lessons_amount")
        instance.lesson_duration = validated_data.get("lesson_duration")

        instance.save()
        return instance

    def save(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return super(CourseSerializer, self).save(*args, **kwargs)