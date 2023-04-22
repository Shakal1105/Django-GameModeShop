from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Key


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'game': {
        'Платформа': 'platform',
        'Жанр': 'genre',
        'Издатель': 'author',
        'Язык': 'language',
        'Дата выхода': 'relise',
        'Версия продукта': 'version'
    },
    'games': {
        'Платформа': 'platform',
        'Жанр': 'genre',
        'Издатель': 'author',
        'Язык': 'language',
        'Дата выхода': 'relise',
        'Версия продукта': 'version'
    },
    'key': {
        'Жанр': 'genre',
        'Язык': 'language',
        'Разработчик': 'author',
        'Серия игр': 'activate',
        'ОС': 'os',
        'Активация': 'is_key',
        'Метод активации': 'num_of_keys',
        'Дата выхода': 'relise',
        'Версия продукта': 'version'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    try:
        for name, value in PRODUCT_SPEC[model_name].items():
            table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
        return table_content
    except KeyError:
        pass


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Key):
        if not product.is_key:
            PRODUCT_SPEC['key'].pop('Метод активации', None)
        else:
            PRODUCT_SPEC['key']['Метод активации'] = 'num_of_keys'
    try:
        return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
    except TypeError:
        pass
