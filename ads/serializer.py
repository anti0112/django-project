from importlib.metadata import requires
from rest_framework import serializers
from ads.models import Ad, Category, Selections
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"    
    

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryUpdateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Category
        fields = "__all__"

class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
            
class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,slug_field='username',)
    category = serializers.SlugRelatedField(read_only=True,slug_field='name',)
    
    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,slug_field='username',)
    category = serializers.SlugRelatedField(read_only=True,slug_field='name',)
    
    class Meta:
        model = Ad
        fields = ['Id', 'name', 'author', 'price', 'description', 'is_published', 'image', 'category']
        

class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ['Id', 'image']
        

class AdDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
        

class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selections
        fields = ['id','name']


class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
    )
    items = AdDetailSerializer(many=True)
    class Meta:
        model = Selections
        fields = "__all__"
        
class SelectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selections
        fields = "__all__"
        
        
class SelectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selections
        fields = "__all__"


class SelectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selections
        fields = "__all__"