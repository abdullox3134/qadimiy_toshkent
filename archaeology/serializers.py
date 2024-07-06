from rest_framework import serializers
from archaeology.models import Archaeology, Items, News, ArchaeologyPicture, \
    ItemsPicture, NewsPicture, ItemsVideo


# class RegionSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Region
#         fields = ['id', 'title_uz', 'title_en', 'longitude', 'latitude']


# class ArchaeologyVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArchaeologyVideo
#         fields = ['id', 'video', 'link',]


class ArchaeologyPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchaeologyPicture
        fields = ['id', 'image', 'link',]


class ArchaeologySerializers(serializers.ModelSerializer):
    # archaeologyVideo = serializers.SerializerMethodField()
    archaeologyPicture = serializers.SerializerMethodField()
    class Meta:
        model = Archaeology
        fields = ['id', 'title_uz', 'title_en', 'context_uz', 'context_en',
                  'video', 'link', 'create', 'update', 'archaeologyPicture']

    # def get_archaeologyVideo(self, obj):
    #     request = self.context.get('request')
    #     data = ArchaeologyVideoSerializer(obj.archaeologyVideo.all(), many=True, context={'request': request}).data
    #     for obj_url in data:
    #         if obj_url.get('video') and request is not None:
    #             obj_url['video'] = request.build_absolute_uri(obj_url['video'])
    #     return data

    def get_archaeologyPicture(self, obj):
        request = self.context.get('request')
        data = ArchaeologyPictureSerializer(obj.archaeologyPicture.all(), many=True, context={'request': request}).data
        for obj_url in data:
            if obj_url.get('image') and request is not None:
                obj_url['image'] = request.build_absolute_uri(obj_url['image'])
        return data


# class ArchaeologyLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Archaeology
#         fields = ['id', 'like', ]


class ItemsPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsPicture
        fields = ['id', 'image', 'link',]


# class ItemsVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ItemsVideo
#         fields = ['video', 'link',]


class ItemsSerializers(serializers.ModelSerializer):
    picture_items = serializers.SerializerMethodField()
    # video_items = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ['id',
            'title_uz', 'title_en', 'context_uz', 'context_en',
            'video', 'create', 'update', 'picture_items',]

    def get_picture_items(self, obj):
        request = self.context.get('request')
        data = ItemsPictureSerializer(obj.picture_items.all(), many=True, context={'request': request}).data
        for obj_url in data:
            if obj_url.get('image') and request is not None:
                obj_url['image'] = request.build_absolute_uri(obj_url['image'])
        return data

    # def get_video_items(self, obj):
    #     request = self.context.get('request')
    #     data = ItemsVideoSerializer(obj.video_items.all(), many=True, context={'request': request}).data
    #     for obj_url in data:
    #         if obj_url.get('video') and request is not None:
    #             obj_url['video'] = request.build_absolute_uri(obj_url['video'])
    #     return data


# class ItemsLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Items
#         fields = ['id', 'like', ]


class NewsPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPicture
        fields = ['id', 'image',]


# class NewsVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewsVideo
#         fields = ['id', 'video', 'link', 'title_uz', 'title_en',]


class NewsSerializers(serializers.ModelSerializer):
    news_picture = NewsPictureSerializer(many=True, read_only=True)
    # news_video = NewsVideoSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title_uz', 'title_en', 'context_uz', 'context_en', 'create', 'update', 'news_picture',)


# class SubVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubVideo
#         fields = ['id', 'video', 'link']


# class VideoSerializers(serializers.ModelSerializer):
#     sub_video = SubVideoSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Video
#         fields = ('id', 'title_uz', 'title_en', 'sub_video')


# class SubPictureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubPicture
#         fields = ['id', 'image', 'link']



# class PictureSerializers(serializers.ModelSerializer):
#     sub_picture = SubPictureSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Picture
#         fields = ('id', 'title_uz', 'title_en', 'sub_picture')
