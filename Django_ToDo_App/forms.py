from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs=
        {
            "placeholder": "Enter a Task",
            "class": "form-control",
            "autofocus": True,
        }
        ) )

    # noinspection PyUnusedClass
    class Meta:
        model = Task
        fields = ("title",)
    # Forms.py is used to define and manage Django forms, which are Python classes that represent HTML forms. These forms can be used to handle user input, validate data, and interact with the database.
