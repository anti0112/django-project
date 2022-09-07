from users.models import User, Location
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = User
        exclude = ['password']
        

class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    
    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop('location', None)
        return super().is_valid(raise_exception=raise_exception)
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        
        user.set_password(validated_data['password'])
        user.save()
        if self._location:
            location_obj = Location.objects.get_or_create(name=self._location)[0]
            user.location = location_obj
            user.save()
        return user
    

class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=False, 
        slug_field='name', 
        queryset=Location.objects.all()
    )
    
    class Meta:
        model = User
        exclude = ['id']
        
    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop('location', None)
        return super().is_valid(raise_exception=raise_exception)
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        if self._location:
            location_obj = Location.objects.get_or_create(name=self._location)[0]
            user.location = location_obj
            user.save()
        return user
    
class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
        