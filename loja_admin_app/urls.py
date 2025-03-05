from django.urls import path
from .views import *
from . import views

app_name= 'loja_admin_app'

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('produtos/', ProdutosView.as_view(), name= 'produtos'),

    
    path('pagamento/<int:produto_id>/', pagamento_view, name='pagamento'),

    path('sucesso_pagamento/', SucessoPagamentoView.as_view(), name='sucesso_pagamento'),
    path('produtos_logado/', views.produtos_logado_view, name='produtos_logado'),
    path('home_logado/', views.home_logado_view, name='home_logado'),
    path('sem_permissao/', views.sem_permissao, name='sem_permissao'),
]