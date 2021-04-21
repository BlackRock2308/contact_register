from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label= "Nom utilisateurs",
                                widget= forms.TextInput(
                                    attrs= {
                                        "class" : "form-control"
                                    }
                                ))
    password = forms.CharField(label= "Mot de passe",
                                widget= forms.PasswordInput(
                                    attrs= {
                                        "class" : "form-control"
                                    }
                                )) 