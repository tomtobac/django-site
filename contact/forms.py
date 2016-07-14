from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Some text'
        })
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_name'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Name'
            })
        self.fields['contact_email'].label = "Your email:"
        self.fields['contact_email'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Email'
            })
        self.fields['content'].label = "What do you want to say?"
