from django import forms


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    user = forms.CharField(label='Name')
    email = forms.CharField(label='E-mail',widget=forms.EmailInput)
    content = forms.CharField(label='Comment',widget=forms.Textarea)