from django.forms import ModelForm
from .models import *


class addQusetionform(ModelForm):
    class Meta:
        model = QuesModel
        fields = '__all__'