from django.contrib import admin
from django.urls import path
from produtos.views import (
    listar_produtos,
    criar_produto,
    editar_produto,
    excluir_produto,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", listar_produtos, name="listar_produtos"),
    path("produtos/novo/", criar_produto, name="criar_produto"),
    path("produtos/<int:id>/editar/", editar_produto, name="editar_produto"),
    path("produtos/<int:id>/excluir/", excluir_produto, name="excluir_produto"),
]