# from tortoise import fields
# from tortoise.models import Model
# from app.db.mixin import TimestampMixin, BaseModel

# class Faq(BaseModel, TimestampMixin):
#     question = fields.TextField()
#     answer = fields.TextField()
#     is_active = fields.BooleanField(default=True)
#     order = fields.IntField()

#     class Meta:
#         table = "faqs"
#         table_description = "Вопросы и ответы"

#     def __str__(self):
#         return self.question
    
# class Slider(BaseModel, TimestampMixin):
#     title = fields.CharField(max_length=255)
#     description = fields.TextField(null=True)
#     image = fields.CharField(max_length=255)
#     link = fields.CharField(max_length=255, null=True)
#     is_active = fields.BooleanField(default=True)
#     order = fields.IntField()

#     class Meta:
#         table = "sliders"
#         table_description = "Слайдер"

#     def __str__(self):
#         return self.title