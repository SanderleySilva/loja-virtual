from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from .models import Produto, Pedido, Categoria
from .forms import PagamentoForm
from django.conf import settings

class HomeView(TemplateView):
    template_name = 'estilos/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        return context
    


class ProdutosView(TemplateView):
    template_name = 'produtos/produtos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.all()
        return context
        
    

from django.shortcuts import render, redirect, get_object_or_404
from django.template.context import RequestContext
from django.views.decorators.http import require_http_methods
from .models import Produto
from .forms import PagamentoForm

@require_http_methods(["GET", "POST"])
def pagamento_view(request, produto_id):
    if not request.user.is_authenticated:
        return redirect('login')

    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'GET':
        form = PagamentoForm()
        context = {
            'produto': produto,
            'form': form
        }
        return render(request, 'pagamentos/pagamento.html', context)

    elif request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.produto = produto
            pedido.save()
            # Adicione a lógica para processar o pagamento (Pix ou Cartão) aqui
            return redirect('loja_admin_app:sucesso_pagamento')
        context = {
            'produto': produto,
            'form': form
        }
        return render(request, 'pagamentos/pagamento.html', context)


class SucessoPagamentoView(TemplateView):
    template_name = 'pagamentos/sucesso_pagamento.html'


def sem_permissao(request):
    return render(request, 'sempermissao.html')

def produtos_logado_view(request):
    if request.user.is_authenticated:
        categorias = Categoria.objects.all()
        return render(request, 'aposlogado/produtoslogado.html', {'categoria': categorias})
    else:
        return redirect('loja_admin_app:sem_permissao')
    


def home_logado_view(request):
    context = {
        'produtos': Produto.objects.all(),
    }
    return render(request, 'estilos/home.html', context)


