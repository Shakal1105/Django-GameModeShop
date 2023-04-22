from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin
from .models import *

class KeyAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and not instance.is_key:
            self.fields['num_of_keys'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })

    def clean(self):
        if not self.cleaned_data['is_key']:
            self.cleaned_data['num_of_keys'] = None
        return self.cleaned_data


class GameAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='game'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class GamesAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='games'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class KeyAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = KeyAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='key'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(Game, GameAdmin)
admin.site.register(Games, GamesAdmin)
admin.site.register(Key, KeyAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)

