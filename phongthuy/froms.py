from django import forms

from phongthuy.models import Datapt


class simphongthuy(forms.ModelForm):
    class Meta:
        model = Datapt
        fields= ("__all__")

    def is_valid(self):
        valid = super(simphongthuy, self).is_valid()
        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        pt = super(simphongthuy, self).save(commit=False)
        if commit:
            pt.save()
        return pt