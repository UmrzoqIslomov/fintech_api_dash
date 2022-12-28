from rest_framework import serializers

from apps.teachers.models.teachers import TeacherModel


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.image = validated_data.get("image")
        instance.teacher = validated_data.get("teacher")
        instance.course = validated_data.get("course")
        instance.about = validated_data.get("about")
        instance.experience = validated_data.get("experience")
        instance.social_network1 = validated_data.get("social_network1")
        instance.social_network2 = validated_data.get("social_network2")
        instance.social_network3 = validated_data.get("social_network3")
        instance.social_network4 = validated_data.get("social_network4")
        instance.rating = validated_data.get("rating")
        instance.rating = validated_data.get("rating")
        instance.teacher_level = validated_data.get("teacher_level")

        instance.save()
        return instance

    def save(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return super(TeacherSerializer, self).save(*args, **kwargs)