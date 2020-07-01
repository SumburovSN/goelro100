from django import forms
from . import info


class Quiz(forms.Form):

    # def __init__(self):
    #     super()
    #     quiz = info.quiz1
    #
    #     for question in quiz:
    #         i = 0
    #         responses = []
    #         for response in question[1]:
    #             responses.append((i, response))
    #             i += 1
    #         self.fields.append(forms.ChoiceField(
    #             choices=responses,
    #             required=False,
    #             label=question[0],
    #             help_text="Click to select your choice",
    #             widget=forms.RadioSelect
    #         ))
    #         print(self.fields)

    quiz = info.quiz1
    question = []
    responses0 = [(1, quiz[0][1][0]), (2, quiz[0][1][1]), (3, quiz[0][1][2]), (4, quiz[0][1][3])]
    question0 = forms.ChoiceField(
        choices=responses0,
        required=False,
        label=quiz[0][0],
        help_text="Click to select your choice",
        widget=forms.RadioSelect
        )
    responses1 = [(1, quiz[1][1][0]), (2, quiz[1][1][1]), (3, quiz[1][1][2]), (4, quiz[1][1][3])]
    question1 = forms.ChoiceField(
        choices=responses1,
        required=False,
        label=quiz[1][0],
        help_text="Click to select your choice",
        widget=forms.RadioSelect
    )