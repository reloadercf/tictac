from django.forms import ModelForm
from django.core.exceptions import ValidationError


from .models import Move
class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = []

    def clean (self):
        x=self.cleaned_data.get("x")
        y=self.cleaned_data.get("y")
        game=self.instance.game
        try:
            if game.board()[y][x]is not None:
                raise ValidationError ("El cuadro no puede estar vacio")
        except IndexError:
            raise ValidationError("Coordenadas  invalidas")
        return self.cleaned_data
