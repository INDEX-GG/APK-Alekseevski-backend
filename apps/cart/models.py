from django.db import models


class Order(models.Model):

    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


# "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NDYwNDk4NywianRpIjoiZjdmYzc0YzRkZGUyNGNlMWE1ODg4NWVjNDg3YTg4YTAiLCJ1c2VyX2lkIjoxfQ.CXZ8ItCCBcrCsWQrnEsCO3qjh_t-eWlBvjwxXpDp6Sk",
