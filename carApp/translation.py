from modeltranslation.translator import register,TranslationOptions
from .models import Car


@register(Car)
class CarTranslationOptions(TranslationOptions):
	fields=('name','model','desc')
