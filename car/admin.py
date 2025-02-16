from django.contrib import admin
from .models import Users , Car , Diameter , Body ,TypeCar , CarInstance
from .models import News
# Register your models here.
# from .models import Post

# from django.utils.html import format_html


class carInstanceInlines(admin.TabularInline):
    model = CarInstance
# admin.py
from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Customize the fields shown in the admin panel        
@admin.register(Car)

class CarAdmin(admin.ModelAdmin) :
    list_display = ('CarModel','dateOfIndustry','Engine','gearBox','Wheel','price')    
    list_filter = ('CarModel',)
    search_fields = ['CarModel']
    inlines = [carInstanceInlines]


    

    

