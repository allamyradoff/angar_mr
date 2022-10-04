from django import forms
from .models import *



# class DukanForm(forms.ModelForm):
#     class Meta:
#         model = Dukanlar
#         fields = ['ady', 'welayat', 'salgy', 'tel1', 'tel2', 'geo']
        




#         widgets = {
#             "name":forms.TextInput(attrs={'class':"sm-form-control require", 'placeholder':"example@gmail.com"}),
#             "welayat":forms.TextInput(attrs={'class':"sm-form-control require", 'placeholder':"Anna Myradow"}),
#             "address":forms.TextInput(attrs={'class':"sm-form-control require", 'placeholder':"+99361234567"}),
#             "phone_first":forms.TextInput(attrs={'class':"required sm-form-control", 'placeholder':". . ."}),
#             "phone_second":forms.TextInput(attrs={'class':"required sm-form-control", 'placeholder':". . ."}),
#             "geo":forms.TextInput(attrs={'class':"required sm-form-control", 'placeholder':". . ."}),
#         }


class ZapcasForm(forms.ModelForm):
    class Meta:
        model = Zapcas
        fields = ['title', 'priceman', 'notes', 'carids', 'catid', 'yagday', 'tel']
        




        widgets = {
            "title":forms.TextInput(attrs={'class':"form-control", }),
            "priceman":forms.TextInput(attrs={'class':"form-control", }),
            "notes":forms.TextInput(attrs={'class':"form-control", }),
            "carids":forms.TextInput(attrs={'class':"form-control", 'id':"carid"}),
            "catid":forms.TextInput(attrs={'class':"form-control", 'id':"catid", }),
            "yagday":forms.TextInput(attrs={'class':"form-control", }),
            "tel":forms.TextInput(attrs={'class':"form-control", }),
        }
        
class CarsForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['id', 'name',]
        




        widgets = {
            "id":forms.TextInput(attrs={'class':"form-control", }),
            "name":forms.TextInput(attrs={'class':"form-control", }),

        }