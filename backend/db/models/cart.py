# from tortoise.models import Model
# from tortoise import fields
# from datetime import datetime
# from app.db.mixin import TimestampMixin, BaseModel

# class Cart(BaseModel, TimestampMixin):
#     user = fields.ForeignKeyField("models.User", related_name="carts", on_delete=fields.CASCADE)
#     quantity = fields.IntField()
#     promocode = fields.ForeignKeyField("models.Promocode", related_name="carts", null=True)

#     class Meta:
#         table = "carts"
#         table_description = "Корзины"

#     def __str__(self):
#         return f"{self.user.username} - {self.product.name} - {self.quantity}"
    
# class CartItem(BaseModel, TimestampMixin):
#     cart = fields.ForeignKeyField("models.Cart", related_name="items", on_delete=fields.CASCADE)
#     product_variant = fields.ForeignKeyField("models.ProductVariant", related_name="carts", on_delete=fields.CASCADE)
#     quantity = fields.IntField()

#     class Meta:
#         table = "cart_items"
#         table_description = "Товары в корзине"

#     def __str__(self):
#         return f"{self.cart.user.username} - {self.product.name} - {self.quantity}"

# class Promocode(BaseModel, TimestampMixin):
#     code = fields.CharField(max_length=255, unique=True)
#     min_order_price = fields.IntField()
#     discount = fields.IntField()
#     percent = fields.BooleanField()
#     activations = fields.IntField(default=0)
#     max_activations = fields.IntField(null=True)
#     one_time = fields.BooleanField()
#     start_date = fields.DatetimeField(default=datetime.now)
#     end_date = fields.DatetimeField()

#     class Meta:
#         table = "promocodes"
#         table_description = "Промокоды"

#     def __str__(self):
#         return self.code