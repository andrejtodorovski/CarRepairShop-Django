from django.forms import ModelForm

from .models import Repair


class RepairModelForm(ModelForm):
    class Meta:
        model = Repair
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
