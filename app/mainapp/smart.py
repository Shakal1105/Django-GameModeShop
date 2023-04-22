from django.db.models import Count
from mainapp.models import *

# Получаем queryset с агрегированными данными
product_counts = CartProduct.objects.annotate(num_orders=Count('cart')).order_by('-num_orders')

# Выводим на экран список товаров с количеством заказов
for product in product_counts:
    print(f'{product.content_object.title}: {product.num_orders} заказов')
