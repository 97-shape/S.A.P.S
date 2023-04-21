from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

from database.models import Board

class BoardWriteForm(forms.ModelForm):

    title = forms.CharField(
        label = "제목",
        widget = forms.TextInput(
            attrs = {
                'placeholder' : '게시글 제목',
                'class' : 'form-control mb-2'
            }
        ), required=True,
    )

    content = SummernoteTextField()

    field_order = [
        'title',
        'content',
    ]

    class Meta:
        model = Board
        fields = [
            'title',
            'content',
        ]
        widgets = {
            'content' :  SummernoteWidget()
        }

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        content = cleaned_data.get('content', '')

        if title == '':
            self.add_error('title', '제목을 입력하세요')
        elif content == '':
            self.add_error('content', '글 내용을 입력하세요')
        else:
            self.title = title
            self.content = content