from django import forms
from scoresheet.models import FileStoreage


class DocumentForm(forms.ModelForm):
    class Meta:
        model = FileStoreage
        fields = ('document', )