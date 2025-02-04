# from tortoise import fields
# from tortoise.models import Model
# from app.db.mixin import TimestampMixin, BaseModel
    
# class Order(BaseModel, TimestampMixin):
#     id = fields.IntField(pk=True)
#     user = fields.ForeignKeyField("models.User", related_name="orders", on_delete=fields.CASCADE)
#     order_status = fields.ForeignKeyField("models.OrderStatus", related_name="orders", on_delete=fields.CASCADE)
#     payment_type = fields.ForeignKeyField("models.PaymentType", related_name="orders", on_delete=fields.CASCADE)
#     delivery_method = fields.ForeignKeyField("models.DeliveryMethod", related_name="orders", on_delete=fields.CASCADE)
#     address = fields.TextField()
#     city = fields.CharField(max_length=255)
#     store = fields.ForeignKeyField("models.Store", related_name="orders", null=True)
#     pickup_point = fields.ForeignKeyField("models.PickupPoint", related_name="orders", null=True)

#     class Meta:
#         table = "orders"
#         table_description = "Заказы"

#     def __str__(self):
#         return self.order_id
    
# class PickupPoint(BaseModel, TimestampMixin):
#     id = fields.IntField(pk=True)
#     city = fields.CharField(max_length=255)
#     address = fields.TextField()
#     provider = fields.CharField(max_length=255)
#     point_id = fields.CharField(max_length=255)
#     latitude = fields.CharField(max_length=255)
#     longitude = fields.CharField(max_length=255)
#     is_active = fields.BooleanField(default=True)

#     class Meta:
#         table = "pickup_points"
#         table_description = "Пункты самовывоза"

#     def __str__(self):
#         return self.address
    
# class Recipient(BaseModel, TimestampMixin):
#     id = fields.IntField(pk=True)
#     order = fields.ForeignKeyField("models.Order", related_name="recipients", on_delete=fields.CASCADE)
#     first_name = fields.CharField(max_length=255)
#     middle_name = fields.CharField(max_length=255, null=True)
#     last_name = fields.CharField(max_length=255)
#     phone = fields.CharField(max_length=20)
#     email = fields.CharField(max_length=255)

#     class Meta:
#         table = "recipients"
#         table_description = "Получатели"

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
# class OrderItem(BaseModel, TimestampMixin):
#     order = fields.ForeignKeyField("models.Order", related_name="items", on_delete=fields.CASCADE)
#     product_variant = fields.ForeignKeyField("models.ProductVariant", related_name="orders", on_delete=fields.CASCADE)
#     quantity = fields.IntField()

#     class Meta:
#         table = "order_items"
#         table_description = "Товары в заказе"

#     def __str__(self):
#         return f"{self.order.order_id} - {self.product.name} - {self.quantity}"
    
# class PaymentType(BaseModel, TimestampMixin):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=255)
#     description = fields.TextField(null=True)
#     is_active = fields.BooleanField(default=True)

#     class Meta:
#         table = "payment_types"
#         table_description = "Типы оплаты"

#     def __str__(self):
#         return self.name

# class DeliveryMethod(BaseModel, TimestampMixin):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=255)
#     description = fields.TextField(null=True)
#     is_active = fields.BooleanField(default=True)
#     payment_types = fields.ManyToManyField("models.PaymentType", related_name="delivery_methods")

#     class Meta:
#         table = "delivery_methods"
#         table_description = "Способы доставки"

#     def __str__(self):
#         return self.name

# class OrderStatus(BaseModel, TimestampMixin):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=255)
#     description = fields.TextField(null=True)

#     class Meta:
#         table = "order_statuses"
#         table_description = "Статусы заказов"

#     def __str__(self):
#         return self.name
    
