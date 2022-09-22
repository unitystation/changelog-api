from rest_framework import serializers
from ..models import Change, BuildVersion
from django.conf import settings

def validate_secret_token(value: str) -> str:
    if value != settings.SECRET_KEY:
        raise serializers.ValidationError("Invalid secret token!")
    return value


class PostBuildVersionSerializer(serializers.ModelSerializer):
    secret_token = serializers.CharField(write_only=True)

    class Meta:
        model = BuildVersion
        fields = ('version_number', 'date_created', 'secret_token')

    def validate_secret_token(self, value: str) -> str:
        return validate_secret_token(value)

    def create(self, validated_data):
        validated_data.pop('secret_token')
        return super().create(validated_data)


class PostChangeSerializer(serializers.ModelSerializer):
    secret_token = serializers.CharField(write_only=True)

    class Meta:
        model = Change
        fields = ('author_username', 'author_url', 'description', 'pr_url', 'pr_number', 'category', 'secret_token')

    def validate_secret_token(self, value: str) -> str:
        return validate_secret_token(value)

    def create(self, validated_data):
        validated_data.pop('secret_token')
        return super().create(validated_data)


class PostChangeWithBuildSerialiazer(serializers.ModelSerializer):
    secret_token = serializers.CharField(write_only=True)

    class Meta:
        model = Change
        fields = ('author_username', 'author_url', 'description', 'pr_url', 'pr_number', 'category', 'build', 'date_added', 'secret_token')

    def validate_secret_token(self, value: str) -> str:
        return validate_secret_token(value)

    def create(self, validated_data):
        validated_data.pop('secret_token')
        return super().create(validated_data)


class GetChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = ('author_username', 'author_url', 'description', 'pr_url', 'pr_number', 'category', 'build', 'date_added')


class GetBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildVersion
        fields = ('version_number', 'date_created')

class GetAllChangesSerializer(serializers.ModelSerializer):
    changes = GetChangeSerializer(many=True, read_only=True)
    class Meta:
        model = BuildVersion
        fields = ('version_number', 'date_created', 'changes')