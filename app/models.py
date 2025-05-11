from django.db import models

CATEGORY_CHOICES = [
    ('CR', 'Curd'),
    ('DS', 'Dahi'),
    ('CH', 'Cheese'),
    ('YH', 'Yogurt'),
    ('BT', 'Butter'),
    ('CM', 'Cream'),
    ('PW', 'Paneer Whey'),
    ('WH', 'Whey'),
    ('GH', 'Ghee'),
    ('ML', 'Milk'),
    ('IC', 'Ice Cream'),
    ('PN', 'Paneer'),
]

class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')
    def __str__(self):
        return self.title 
