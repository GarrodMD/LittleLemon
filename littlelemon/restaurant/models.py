from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.PositiveIntegerField()
    BookingDate = models.DateTimeField()

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'
    
    def __str__(self):
        return f'{self.Name} for {self.No_of_guests} guests on {self.BookingDate}'

# Add code to create Menu model
class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'
        
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
