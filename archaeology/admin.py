from django.contrib import admin

from .models import Archaeology, Items, News, ArchaeologyPicture, \
    NewsPicture, ItemsPicture, ItemsVideo


# class NewsVideoTabularInline(admin.TabularInline):
#     model = NewsVideo
#     fields = ['title_uz', 'title_en', 'link', 'video']


class NewsPictureTabularInline(admin.TabularInline):
    model = NewsPicture
    fields = ['image']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # inlines = [NewsVideoTabularInline, NewsPictureTabularInline]
    inlines = [NewsPictureTabularInline]
    fields = ['title_uz', 'title_en', 'context_uz', 'context_en', 'image',]


class items_Video(admin.TabularInline):
    model = ItemsVideo
    fields = ['link', 'video']


class items_Picture(admin.TabularInline):
    model = ItemsPicture
    fields = ['link', 'image']


@admin.register(Items)
class itemsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [items_Picture]
    fields = ('context_uz', 'context_en', 'title_uz', 'title_en', 'image', 'video', 'video_link', 'link',)



# class Archaeology_Video(admin.TabularInline):
#     model = ArchaeologyVideo
#     fields = ['title_uz', 'title_en', 'link', 'video']


class Archaeology_Picture(admin.TabularInline):
    model = ArchaeologyPicture
    fields = ['link', 'image']


@admin.register(Archaeology)
class ArchaeologyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # inlines = [Archaeology_Video, Archaeology_Picture]
    inlines = [Archaeology_Picture]
    fields = ('context_uz', 'context_en', 'title_uz', 'title_en', 'image', 'video', 'video_link', 'link',)

