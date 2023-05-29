from django.db import models

# 用户表  
class User(models.Model):  
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=100)  
    password = models.CharField(max_length=100)  
    role = models.CharField(max_length=10, choices=[('user', 'user')])  

# 航班表  
class Flight(models.Model): 
    id = models.IntegerField(primary_key=True)  
    #airline = models.ForeignKey("Airline", on_delete=models.CASCADE) 
    departure_city = models.CharField(max_length=50)  
    arrival_city = models.CharField(max_length=50)  
    departure_time = models.DateTimeField()  
    arrival_time = models.DateTimeField()
    ticket_type = models.CharField(max_length=10)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    options = [('first', 'first'), ('business', 'business'), ('economy', 'economy')]

# 订单表  
class Order(models.Model):  
    id = models.IntegerField(primary_key=True) 
    #staff = models.ForeignKey("Staff", on_delete=models.CASCADE)  
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE)  
    ticket_type = models.CharField(max_length=10, choices=Flight.options)  
    is_rebooked = models.BooleanField()  

# 代表表  
class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    #airline = models.ForeignKey("Airline", on_delete=models.CASCADE)

# 机票表     
class Ticket(models.Model):  
    id = models.IntegerField(primary_key=True) 
    order = models.ForeignKey("Order", on_delete=models.CASCADE)  
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE)  
    status = models.CharField(max_length=10, choices=[('available', 'available'), ('issued', 'issued')])

# 改签订单表  
class RebookOrder(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)  
    new_flight = models.ForeignKey("Flight", on_delete=models.CASCADE)  
    new_ticket_type = models.CharField(max_length=10, choices=Flight.options)  
