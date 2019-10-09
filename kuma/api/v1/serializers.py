from rest_framework import exceptions
from rest_framework import serializers

from kuma.wiki.models import BCSignal, Document


class BCSignalSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(max_length=255)
    locale = serializers.CharField(max_length=255)
    explanation = CharField(
        allow_blank=True, required=False, max_length=1000
    )
    supporting_material = CharField(
        allow_blank=True, required=False, max_length=1000
    )

    class Meta:
        model = BCSignal
        fields = (
            'slug', 'locale', 'browsers',
            'feature', 'explanation', 'supporting_material'
        )

    def create(self, validated_data):
        slug = validated_data.pop('slug')
        locale = validated_data.pop('locale')
        document = Document.objects.filter(slug=slug, locale=locale).first()

        if document:
            return BCSignal.objects.create(document=document, **validated_data)
        raise exceptions.ValidationError('Document not found')
