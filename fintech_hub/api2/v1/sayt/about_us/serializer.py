from rest_framework import serializers

from apps.about_us.models.about_us import AboutUsModel


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsModel
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.body = validated_data.get("body")
        instance.title = validated_data.get("title")
        instance.image1 = validated_data.get("image1")
        instance.image2 = validated_data.get("image2")

        instance.save()
        return instance

    def save(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return super(AboutSerializer, self).save(*args, **kwargs)
