from django import forms
"""
This form allows users to select a quantity of 
products and add it to the cart.
"""

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )
    override = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)