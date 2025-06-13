from django import forms        
from .models import expense
class ItemForm(forms.Form):
    Expense_reason=forms.CharField(label=" Your Expense")
    Amount=forms.FloatField(label="Amount")
    Image=forms.CharField(label="Image")
class ItemFormModel(forms.ModelForm):
    class Meta:
        model=expense
        fields=['Expense_reason', 'Amount', 'Image']
