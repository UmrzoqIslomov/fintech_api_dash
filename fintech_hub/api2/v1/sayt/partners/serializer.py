from rest_framework import serializers

from apps.partners.models.partners import PartnersModel


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersModel
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.image = validated_data.get("image")

        instance.save()
        return instance

    def save(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return super(PartnersSerializer, self).save(*args, **kwargs)