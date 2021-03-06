from django.forms import ModelForm
from petstagram.pets.models import Pet


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_fields()

    def _init_bootstrap_fields(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PetForm(ModelForm, BootstrapFormMixin):
    class Meta:
        model = Pet
        fields = '__all__'