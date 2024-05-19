from django import forms

class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')  # Access the question object
        super().__init__(*args, **kwargs)
        if question:
            self.fields['question_text'] = forms.CharField(label='Question:', disabled=True, initial=question.question_text)
            if question.type == 'TEXT':
                self.fields['answer'] = forms.CharField(label='Answer:')
            elif question.type == 'EMAIL':
                self.fields['answer'] = forms.EmailField(label='Email:')
            elif question.type == 'PHONE':
                self.fields['answer'] = forms.CharField(label='Phone:')
            elif question.type == 'DATE':
                self.fields['answer'] = forms.DateField(label='Date:')
            elif question.type == 'CHOICE':
                self.fields['answer'] = forms.ChoiceField(label='Answer:', choices=question.options)
            else:
                raise ValueError('Invalid question type')
