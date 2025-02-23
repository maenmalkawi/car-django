from django.db import models
import uuid
from django.urls import reverse





# Create your models here.
class Users(models.Model):
    phone= models.DecimalField(max_digits=10,decimal_places=0,help_text="please enter 10 digit phone number ")
    name= models.CharField(max_length=20,help_text="enter your name",verbose_name="this must be your first name")
    country = models.CharField(max_length=20,default="323233",null=False )
    
    def __str__(self) :
     return f'{self.phone}'
 
# models.py

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)  # New image field

   
 
    def get_absolute_url(self):
        return reverse('news', kwargs={'pk': self.pk})  # Replace 'car-detail' with your URL name
 
 
class Car(models.Model):
 # att : car model , engine , gearbox , wheel
    CarModel = models.CharField(max_length=20, help_text="Enter your car model")
    dateOfIndustry = models.DateField(verbose_name="date of industry",help_text="Enter your date of industry")
    Engine = models.CharField(max_length=20, help_text="Enter your Engine power")
    gearBox = models.CharField(max_length=20, help_text="Enter your gearBox type ")
    Wheel = models.CharField(max_length=20, help_text="Enter your wheel type ")
    image = models.ImageField(upload_to='images/',blank=True,null=True)  # New image field
    price = models.CharField(max_length=20, help_text="Enter your price ",blank=True,null=True)

    def get_absolute_url(self):
        return reverse('car', kwargs={'pk': self.pk})  # Replace 'car-detail' with your URL name
    
# ordering 

    class Meta:
            ordering=['CarModel']      
        # always the __STR__ RETYRN A STRING
    def __str__(self):
            return self.CarModel + "" 
     



            
      
class Diameter(models.Model):
 # att : diameter
    Diameter = models.DecimalField( max_digits=10, decimal_places=0,verbose_name="Diameter",help_text="Enter your date of industry")
     
     #Diameter = models.DecimalField(max_digits=10, decimal_places=0, help_text="Enter your Diameter wheel")      
    class Meta:
        ordering=['Diameter']      
    # always the __STR__ RETYRN A STRING
    def __str__(self):
        return f"self.Diameter"


class Body(models.Model): 
    Body = models.CharField(max_length=20, help_text="Enter your car body")

     
        
    class Meta:
        ordering=['Body']      
        #    always the __STR__ RETYRN A STRING
    def __str__(self):
        return self.Body            

class TypeCar(models.Model):
    # att : type , Number of seats , Lighting color , speed 
    # foreign key 
    CarType = models.ForeignKey(Car, on_delete = models.CASCADE ,related_name= 'CarType',)     
    NumberOfSeats = models.DecimalField(max_digits=2, decimal_places=0)
    LightingColor = models.CharField(max_length=20, help_text="Enter your color Of light")
    Speed = models.CharField(max_length=20, help_text="Enter your car speed")
    
    
    class Meta:
        ordering=['CarType']      
    # always the __STR__ RETYRN A STRING
    def __str__(self):
        return f"{self.CarType} {self.Speed}"    
    
class CarInstance(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique id for this car")
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True, related_name="car_instance")
    
    AStatus = (
        ('A', 'AVAILABLE'),
        ('U', 'UNAVAILABLE'), 
    )
    
    status = models.CharField(
        max_length=2, choices=AStatus, blank=True, default='A', help_text="Car availability status"
    )
    
    class Meta:
        ordering = ['Id']
    
    def __str__(self):
        return f'{self.Id} ({self.car.CarType})'
