from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
# from db.models.user_model import User
# from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(max_length=255)
#     password = serializers.CharField()

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(max_length=255)
#     password = serializers.CharField()

# class ResetPasswordSerializer(serializers.Serializer):
#     new_password = serializers.CharField(max_length=40)
#     otp = serializers.CharField(max_length=6)
#     confirm_password = serializers.CharField(max_length=40)

#     def validate(self, attrs):
#         new_password = attrs.get('new_password')
#         confirm_password = attrs.get('confirm_password')
#         if new_password != confirm_password:
#             raise serializers.ValidationError('The new password must match the confirm password')
#         return attrs

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["email", "first_name", "last_name", "password"]

#         # Prevents the password from showing after submission
#         extra_kwargs = {"password": {"write_only": True}}

#     def create(self, validated_data):
#         new_user = User.objects.create(**validated_data)
#         new_user.set_password(validated_data["password"])

#         # Retrieve OTP from view
#         otp = self.context["otp"]
#         new_user.otp = otp
#         new_user.is_individual = True

#         new_user.save()
#         return new_user