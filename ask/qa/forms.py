from django import forms

from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length = 255)
    text = forms.CharField(widget = forms.Textarea)
    def clean(self):
        return self.cleaned_data
    def clean_title(self):
        title = self.cleaned_data['title']
        if title == None or title.strip() == "":
            raise forms.ValidationError
        return title.strip()
    def clean_text(self):
        text = self.cleaned_data['text']
        if text == None or text.strip() == "":
            raise forms.ValidationError
        return text.strip()
    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea)
    question = forms.IntegerField(widget = forms.HiddenInput())
    def clean(self):
        return self.cleaned_data
    def clean_text(self):
        text = self.cleaned_data['text']
        if text == None or text.strip() == "":
            raise forms.ValidationError
        return text.strip()
    def clean_question(self):
         question = self.cleaned_data['question']
         if question == None:
             raise forms.ValidationError
         try:
             question = Question.objects.get(id = int(question))
         except Question.DoesNotExist:
             raise forms.ValidationError
             # question = None
         return question
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer