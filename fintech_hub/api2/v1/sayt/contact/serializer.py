from rest_framework import serializers

from apps.contact.models.contact import ContactModel


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.location = validated_data.get("location")
        instance.social_network1 = validated_data.get("social_network1")
        instance.social_network2 = validated_data.get("social_network2")
        instance.social_network3 = validated_data.get("social_network3")
        instance.social_network4 = validated_data.get("social_network4")
        instance.phone_number = validated_data.get("phone_number")

        instance.save()
        return instance

    def save(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return super(ContactSerializer, self).save(*args, **kwargs)
