
from rest_framework import serializers
from archaeology.models import Region, Archaeology, Items, News, Video, Picture, ArchaeologyVideo, ArchaeologyPicture, \
    ItemsPicture, ItemsVideo, NewsVideo, NewsPicture, SubVideo, SubPicture


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title', 'longitude', 'latitude']


class ArchaeologyVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchaeologyVideo
        fields = ['id', 'video', 'link', 'title']


class ArchaeologyPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchaeologyPicture
        fields = ['id', 'image', 'link', 'title']


class ArchaeologySerializers(serializers.ModelSerializer):
    archaeologyVideo = serializers.SerializerMethodField()
    archaeologyPicture = serializers.SerializerMethodField()

    class Meta:
        model = Archaeology
        fields = ['id', 'title', 'context', 'region', 'password_image', 'downloads',
                  'view_count', 'create', 'update', 'archaeologyVideo', 'archaeologyPicture']

    def get_archaeologyVideo(self, obj):
        request = self.context.get('request')
        data = ArchaeologyVideoSerializer(obj.archaeologyVideo.all(), many=True, context={'request': request}).data
        for obj_url in data:
            if obj_url.get('video') and request is not None:
                obj_url['video'] = request.build_absolute_uri(obj_url['video'])
        return data

    def get_archaeologyPicture(self, obj):
        request = self.context.get('request')
        data = ArchaeologyPictureSerializer(obj.archaeologyPicture.all(), many=True, context={'request': request}).data
        for obj_url in data:
            if obj_url.get('image') and request is not None:
                obj_url['image'] = request.build_absolute_uri(obj_url['image'])
        return data


class ArchaeologyLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archaeology
        fields = ['id', 'like', ]


class ItemsPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsPicture
        fields = ['image', 'link', 'title']


class ItemsVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsVideo
        fields = ['video', 'link', 'title']


class ItemsSerializers(serializers.ModelSerializer):
    picture_items = serializers.SerializerMethodField()
    video_items = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = [
            'title', 'context', 'like', 'password_image', 'downloads',
            'view_count', 'create', 'update', 'picture_items', 'video_items'
        ]

    def get_picture_items(self, obj):
        request = self.context.get('request')
        data = ItemsPictureSerializer(obj.picture_items.all(), many=True, context={'request': request}).data
        for obj_url in data:
            if obj_url.get('image') and request is not None:
                obj_url['image'] = request.build_absolute_uri(obj_url['image'])
        return data

    def get_video_items(self, obj):
        request = self.context.get('request')
        data = ItemsVideoSerializer(obj.video_items.all(), many=True, context={'request': request}).data
        for obj_url in data:
            if obj_url.get('video') and request is not None:
                obj_url['video'] = request.build_absolute_uri(obj_url['video'])
        return data


class ItemsLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id', 'like', ]


class NewsPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPicture
        fields = ['id', 'image', 'link', 'title']


class NewsVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsVideo
        fields = ['id', 'video', 'link', 'title']


class NewsSerializers(serializers.ModelSerializer):
    news_picture = NewsPictureSerializer(many=True, read_only=True)
    news_video = NewsVideoSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'context', 'create', 'update', 'news_video', 'news_picture',)


class SubVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubVideo
        fields = ['id', 'video', 'link']


class VideoSerializers(serializers.ModelSerializer):
    sub_video = SubVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'title', 'sub_video')


class SubPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPicture
        fields = ['id', 'image', 'link']


class PictureSerializers(serializers.ModelSerializer):
    sub_picture = SubPictureSerializer(many=True, read_only=True)

    class Meta:
        model = Picture
        fields = ('id', 'title', 'sub_picture')

