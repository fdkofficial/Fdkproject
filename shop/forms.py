from django import forms
from.models import Book
class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','img_src')
    def __init__(self, *args, **kwargs):
        super(Bookform,self).__init__(*args, **kwargs)
        

        