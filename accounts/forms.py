from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User

INPUT_CLASSES = (
    'block w-full rounded-xl border border-salvia bg-white px-4 py-3 text-base '
    'focus:border-laguna focus:outline focus:outline-2 focus:outline-laguna'
)


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = INPUT_CLASSES


class SignupForm(StyledFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)


class LoginForm(StyledFormMixin, AuthenticationForm):
    pass
