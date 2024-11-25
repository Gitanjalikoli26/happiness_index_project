from django import forms

class profile_form(forms.Form):
    my_choices = (
        ('Student' , 'Student'),
        ('Staff' , 'Staff'),
        ('Other than Teacher Staff' , 'Other than Teacher Staff'),
    )

    fname = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'First Name'}), required=True)
    lname = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Last Name'}), required=True)
    designation = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'email', 'placeholder' : 'Enter Email Address'}), required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'password', 'placeholder' : 'Enter Password'}), required=True)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'password', 'placeholder' : 'Re-Enter Password'}), required=True)

class feedback_form(forms.Form):
    my_choices = (
        ('10' , '10 : Outstanding'),
        ('9' , '9 : Excellent'),
        ('8' , '8 : Very Good'),
        ('7' , '7 : Good'),
        ('6' , '6 : Above Average'),
        ('5' , '5 : Average'),
        ('4' , '4 : Below Average'),
        ('3' , '3 : Weak'),
        ('2' , '2 : Very Weak'),
        ('1' , '1 : Poor'),
    )

    q1 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q2 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q3 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q4 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q5 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q6 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q7 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q8 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q9 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q10 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q11 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q12 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q13 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q14 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    q15 = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices = my_choices, required=True)
    feedback = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Your Feedback'}), required=True)