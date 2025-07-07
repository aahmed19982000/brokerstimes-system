<<<<<<< HEAD
from django import forms
from .models import Site, Official_holiday, CustomHoliday

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'number_of_days', 'start_date','site_link']

class Official_holidayForm(forms.ModelForm):
    class Meta:
        model = Official_holiday
        fields = ['holiday_day']

class CustomHolidayForm(forms.ModelForm):
    class Meta:
        model = CustomHoliday
=======
from django import forms
from .models import Site, Official_holiday, CustomHoliday

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'number_of_days', 'start_date','site_link']

class Official_holidayForm(forms.ModelForm):
    class Meta:
        model = Official_holiday
        fields = ['holiday_day']

class CustomHolidayForm(forms.ModelForm):
    class Meta:
        model = CustomHoliday
>>>>>>> d7023bb44d462afe13064eb16464741bb8208045
        fields = ['user','reason','date']