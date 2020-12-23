from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField()
    # email = forms.EmailField()
    description = forms.CharField()
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "new" not in title:
            raise forms.ValidationError("This is not a valid title.")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
