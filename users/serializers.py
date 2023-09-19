from rest_framework import serializers

from users.models import UserProfile


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "first_name",
            "last_name",
            "user.email",
            "profilePicture",
        ]
