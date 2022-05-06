from decimal import Decimal
from django.conf import settings
from menu.models import Tag


class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, slug, quantity=1, update_quantity=False):

        slug_id = str(slug.id)
        if slug_id not in self.cart:
            self.cart[slug_id] = {'quantity': 0,
                                  'price': str(slug.price)}
        if update_quantity:
            self.cart[slug_id]['quantity'] = quantity
        else:
            self.cart[slug_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, slug):
        slug_id = str(slug.id)
        if slug_id in self.cart:
            del self.cart[slug_id]
            self.save()

    def __iter__(self):
        slug_ids = self.cart.keys()
        slugs = Tag.objects.filter(id__in=slug_ids)
        for slug in slugs:
            self.cart[str(slug.id)]['slug'] = slug

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
