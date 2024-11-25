from django import forms
from django.forms import ModelForm
from .models import Report


class ReportCreateForm(ModelForm):
    class Meta:
        model = Report
        fields = [
            'rua', 'bairro', 'cidade', 'estado', 'cep', 
            'risco_eminente', 'descricao', 'nivel_agua', 
            'moradores_precisam_ajuda', 'categoria', 
            'prioridade'
        ]
        labels = {
            'rua': 'Rua',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'cep': 'CEP',
            'risco_eminente': 'Risco iminente?',
            'descricao': 'Descrição',
            'nivel_agua': 'Nível da água',
            'moradores_precisam_ajuda': 'Moradores precisam de ajuda?',
            'categoria': 'Categoria',
            'prioridade': 'Prioridade',
        }
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva a situação', 'class': 'w-full p-2 border border-gray-300 rounded'}),
            'nivel_agua': forms.TextInput(attrs={'placeholder': 'Ex.: 50 cm', 'class': 'w-full p-2 border border-gray-300 rounded'}),
            'categoria': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'prioridade': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'risco_eminente': forms.CheckboxInput(attrs={'class': 'form-checkbox text-blue-600 mr-2'}),
            'moradores_precisam_ajuda': forms.CheckboxInput(attrs={'class': 'form-checkbox text-blue-600 mr-2'}),
        }


class ReportEditForm(ModelForm):
    class Meta:
        model = Report
        fields = [
            'descricao', 'risco_eminente', 'nivel_agua', 
            'moradores_precisam_ajuda', 'categoria', 
            'prioridade', 'status'
        ]
        labels = {
            'descricao': 'Descrição',
            'risco_eminente': 'Risco iminente?',
            'nivel_agua': 'Nível da água',
            'moradores_precisam_ajuda': 'Moradores precisam de ajuda?',
            'categoria': 'Categoria',
            'prioridade': 'Prioridade',
            'status': 'Status do relato',
        }
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Atualize a descrição', 'class': 'w-full p-2 border border-gray-300 rounded'}),
            'nivel_agua': forms.TextInput(attrs={'placeholder': 'Ex.: 50 cm', 'class': 'w-full p-2 border border-gray-300 rounded'}),
            'categoria': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'prioridade': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'status': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'risco_eminente': forms.CheckboxInput(attrs={'class': 'form-checkbox text-blue-600 mr-2'}),
            'moradores_precisam_ajuda': forms.CheckboxInput(attrs={'class': 'form-checkbox text-blue-600 mr-2'}),
        }
