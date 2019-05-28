from django import forms 

class TodoForm(forms.Form):
    titulo = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Adicione o título de uma task (depois voce pode editar seu conteúdo)', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))


class EditTodoForm(forms.Form):
	edit_titulo = forms.CharField(max_length=40, 
	    widget=forms.TextInput(
	        attrs={'class' : 'form-control', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))
	descricao = forms.CharField(max_length=40, 
	    widget=forms.TextInput(
	        attrs={'class' : 'form-control', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))