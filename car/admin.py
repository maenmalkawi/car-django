from django.contrib import admin
from .models import Users , Car , Diameter , Body ,TypeCar , CarInstance
# Register your models here.
# from .models import Post

# from django.utils.html import format_html
@admin.register(Users)

class UsersAdmin(admin.ModelAdmin) :
    list_display = ('name','country')

class carInstanceInlines(admin.TabularInline):
    model = CarInstance
        
@admin.register(Car)

class CarAdmin(admin.ModelAdmin) :
    list_display = ('CarModel','dateOfIndustry','Engine','gearBox','Wheel',)    
    list_filter = ('CarModel',)
    search_fields = ['CarModel']
    inlines = [carInstanceInlines]
@admin.register(Diameter)

class DiameterAdmin(admin.ModelAdmin) :
    list_display = ('Diameter',)    

@admin.register(Body)

class BodyAdmin(admin.ModelAdmin) :
    list_display = ('Body',)              
    
@admin.register(TypeCar)

class TypeCarAdmin(admin.ModelAdmin) :
    list_display = ('CarType','NumberOfSeats','LightingColor','Speed',)                  
    
@admin.register(CarInstance)

class CarInstanceAdmin(admin.ModelAdmin) :
    list_display = ('Id','car','status',)                      
    list_filter = ('car',)
    search_fields = ['status']
    fieldsets = ( 
        (None,
                 {'fields' : ('Id','car')}),
        ('availabilty',
                 {'fields':('status',)}),


    )
