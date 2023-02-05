from django.forms import ModelForm
from django import forms
from .models import Category, Bookmark, Comment


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['title'].widget.attrs.update({
                "placeholder": "Название категории",
                'class': "input"
        })
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['body'].widget.attrs.update({
                "placeholder": "Краткое описание",
                'class': "textarea"
        })


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = ['title', 'body', 'url', 'tags', 'url_icon']

    def __init__(self, *args, **kwargs):
        super(BookmarkForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['title'].widget.attrs.update({
                "placeholder": "Заголовок",
                'class': "input"
            })

        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['url'].widget.attrs.update({
                "placeholder": "Url адрес",
                'class': "input"
            })
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['url_icon'].widget.attrs.update({
                "placeholder": "Ссылка га партнёрку",
                'class': "input"
            })
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['body'].widget.attrs.update({
                "placeholder": "Описание",
                'class': "textarea"
            })
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['tags'].widget.attrs.update({
                "placeholder": "Добавь теги",
                'class': "input"
            })


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['body'].widget.attrs.update({
                "placeholder": "Написать комментарий",
                'class': "input"
        })













