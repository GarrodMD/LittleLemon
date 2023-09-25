from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.PositiveIntegerField()
    BookingDate= models.DateTimeField()
    
    def __str__(self): 
        return self.Name


# Add code to create Menu model
class Menu(models.Model):
   ID = models.AutoField(primary_key=True)
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2)
   Inventory = models.PositiveIntegerField() 

   def __str__(self):
      return self.title
