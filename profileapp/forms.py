from django.forms import ModelForm


class ProfileCreationform(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']