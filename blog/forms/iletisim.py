from django import forms


class IletisimForm(forms.Form):
    email = forms.EmailField(max_length=250)
    isim_soyisim = forms.CharField(max_length=250)
    mesaj = forms.CharField(widget=forms.Textarea)
