from django import forms
from blog.models import YorumModel


class YorumEkleFormModel(forms.ModelForm):
    class Meta:
        model = YorumModel
        fields = ('yorum',)
