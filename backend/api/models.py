import options as options
from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=100, unique=True, primary_key=True)
  name = models.CharField(max_length=100)
  ID = models.CharField(max_length=100, unique=True)
  password = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  options = [("user", "user"), ("staff", "staff")]
  user_type = models.CharField(max_length=10,  choices=options)


# 航空公司代表表
class Air_Rep(models.Model):
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    co_name = models.CharField(max_length=100)
# # 用户表
# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     role = models.CharField(max_length=10)
#     options = [("user", "user"), ("staff", "staff")]
#
# # 航班表
# class Flight(models.Model):
#     id = models.IntegerField(primary_key=True)
#     airline = models.ForeignKey("Airline", on_delete=models.CASCADE)
#     departure_city = models.CharField(max_length=50)
#     arrival_city = models.CharField(max_length=50)
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     ticket_type = models.CharField(max_length=10)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     options = [("economy", "economy"),("business", "business"), ("first", "first")]
#
# # 订单表
# class Order(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey("User", on_delete=models.CASCADE)
#     flight = models.ForeignKey("Flight", on_delete=models.CASCADE)
#     ticket_type = models.CharField(max_length=10, choices=Flight.options)
#     is_rebooked = models.BooleanField()
#
# # 机票表
# class Ticket(models.Model):
#     id = models.IntegerField(primary_key=True)
#     order = models.ForeignKey("Order", on_delete=models.CASCADE)
#     flight = models.ForeignKey("Flight", on_delete=models.CASCADE)
#     status = models.CharField(max_length=10)
#     options = [('available', 'available'), ('issued', 'issued')]
#
# # 改签订单表
# class RebookOrder(models.Model):
#     order = models.ForeignKey("Order", on_delete=models.CASCADE)
#     new_flight = models.ForeignKey("Flight", on_delete=models.CASCADE)
#     new_ticket_type = models.CharField(max_length=10, choices=Flight.options)
#
# # 航空公司表
# class Airline(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
