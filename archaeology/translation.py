from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import News, NewsPicture, ItemsVideo
from archaeology.models import Archaeology, ArchaeologyPicture, Items, ItemsPicture


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'context',)


@register(Archaeology)
class ArchaeologyTranslationOptions(TranslationOptions):
    fields = ('title', 'context',)


@register(Items)
class ItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'context',)
