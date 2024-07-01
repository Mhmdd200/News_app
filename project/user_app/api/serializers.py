from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {'password':{'write_only':True}}
    def save(self):
        password = self.validated_data['password']
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise ValidationError('This email already exists!')
        account = User(username = self.validated_data['username'], email = self.validated_data['email'])
        account.set_password(password)
        account.save()
        return account
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {'password':{'write_only':True}}
        