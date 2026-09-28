from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "preco", "estoque", "categoria"]

    def clean_preco(self):
        preco = self.cleaned_data["preco"]

        if preco < 0:
            raise forms.ValidationError(
                "O preço não pode ser negativo."
            )

        return preco

    def clean_estoque(self):
        estoque = self.cleaned_data["estoque"]

        if estoque < 0:
            raise forms.ValidationError(
                "O estoque não pode ser negativo."
            )

        return estoque