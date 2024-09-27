from django import forms


from .models import OrderYolzar

class AddressForm(forms.ModelForm):
    class Meta:
        model = OrderYolzar
        fields = ['fname', 'lname', 'country', 'address', 'town_city', 'country_state', 'postcode', 'phone', 'email']