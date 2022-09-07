from django.http import  JsonResponse
from ads.models import Category, Ad, Selections
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from ads.serializer import *
from rest_framework.permissions import IsAuthenticated
from ads.permissions import SelectionUpdatePermission, AdUpdatePermission


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = []
    
class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    permission_classes = [AdUpdatePermission]   
     
class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer
    permission_classes = [AdUpdatePermission]    
        
class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    
    def get(self, request, *args, **kwargs):
        
        category_filter = request.GET.get('category')
        if category_filter:
            self.queryset = self.queryset.filter(category__name__icontains=category_filter)
        
        search_title = request.GET.get('title')
        if search_title:
            self.queryset = self.queryset.filter(name__icontains=search_title)
        
        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)
            
        price_from, price_to = request.GET.get('price_from'), request.GET.get('price_to')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)
        
        return super().get(request, *args, **kwargs)
        
                
class AdDetailView(RetrieveAPIView):
    queryset = Ad
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]
        
class AdCreateView(CreateAPIView):
    queryset = Ad
    serializer_class = AdCreateSerializer
    permission_classes = [AdUpdatePermission]
    
class AdUpdateView(UpdateAPIView):
    queryset = Ad
    serializer_class = AdUpdateSerializer
    permission_classes = [AdUpdatePermission]

class AdDeleteView(DestroyAPIView):
    queryset = Ad
    serializer_class = AdDeleteSerializer
    permission_classes = [AdUpdatePermission]

class SelectionListView(ListAPIView):
    queryset = Selections
    serializer_class = SelectionListSerializer
    

class SelectionDetailView(RetrieveAPIView):
    queryset = Selections
    serializer_class = SelectionDetailSerializer
    permission_classes = [SelectionUpdatePermission]

class SelectionCreateView(CreateAPIView):
    queryset = Selections
    serializer_class = SelectionCreateSerializer
    permission_classes = [SelectionUpdatePermission]
    
class SelectionUpdateView(UpdateAPIView):
    queryset = Selections
    serializer_class = SelectionUpdateSerializer
    permission_classes = [SelectionUpdatePermission]

class SelectionDeleteView(DestroyAPIView):
    queryset = Selections
    serializer_class = SelectionDeleteSerializer
    permission_classes = [SelectionUpdatePermission]  