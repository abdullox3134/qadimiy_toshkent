from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework import status

from archaeology.filters import CategoryFilter
from archaeology.models import Archaeology, Items, News
from archaeology.serializers import ArchaeologySerializers, \
    ItemsSerializers, NewsSerializers


@api_view(['GET'])
@permission_classes([AllowAny])
def archaeology_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    comments = Archaeology.objects.all().order_by("id")
    user_filter = CategoryFilter(request.GET, queryset=comments)
    result_page = paginator.paginate_queryset(user_filter.qs, request)
    serializer = ArchaeologySerializers(result_page, many=True, context={'request': request})
    serializer_url = serializer.data
    for obj_url in serializer_url:
        if obj_url.get('password_image'):
            obj_url['password_image'] = request.build_absolute_uri(obj_url['password_image'])
    return paginator.get_paginated_response(serializer_url)


@api_view(['GET'])
def archaeology_detail(request, pk):
    try:
        archaeology = Archaeology.objects.get(pk=pk)
    except Archaeology.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    archaeology.view_count += 1
    archaeology.save()

    serializer = ArchaeologySerializers(archaeology, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def items_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    comments = Items.objects.all().order_by("id")
    user_filter = CategoryFilter(request.GET, queryset=comments)
    result_page = paginator.paginate_queryset(user_filter.qs, request)
    serializer = ItemsSerializers(result_page, many=True, context={'request': request})
    serializer_url = serializer.data
    for obj_url in serializer_url:
        if obj_url.get('password_image'):
            obj_url['password_image'] = request.build_absolute_uri(obj_url['password_image'])
    return paginator.get_paginated_response(serializer_url)


@api_view(['GET'])
def items_detail(request, pk):
    try:
        items = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    items.view_count += 1
    items.save()

    serializer = ItemsSerializers(items, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def news_list(request):
    comments = News.objects.all().order_by("id")
    serializer = NewsSerializers(comments, many=True)
    serializer_url = serializer.data
    for obj_url in serializer_url:
        for obj in obj_url['news_picture']:
            if obj.get('image'):
                obj['image'] = request.build_absolute_uri(obj['image'])
    return Response(serializer_url)


@api_view(['GET'])
def news_detail(request, pk):
    try:
        about = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NewsSerializers(about)
    serializer_data = serializer.data

    # Tasvir URL'larini absolyut URL'ga aylantirish
    if 'news_picture' in serializer_data:
        for obj in serializer_data['news_picture']:
            if obj.get('image'):
                obj['image'] = request.build_absolute_uri(obj['image'])

    return Response(serializer_data)
