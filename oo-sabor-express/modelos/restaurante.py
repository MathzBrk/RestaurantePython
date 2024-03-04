from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    '''
    A classe irá fazer mostrar tudo sobre os restaurantes
    '''
    restaurantes = []
    def __init__(self, nome, categoria):
        '''
        É o construtor da nossa classe Restaurante, que recebe o nome e a categoria
        '''
        self._nome = nome.title()
        self._category = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._category}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''
        Função que intera sobre a lista de restaurantes, mostrando todos os que tem
        '''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._category.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')


    @property
    def ativo(self):
        '''
        Se o restaurante estiver ativo, mostra um verificado, senão mostra um X
        '''
        return  '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        '''
        Alterna o status do restaurante
        '''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''
        Função que recebe a avaliação
        input = cliente(str) e nota

        output = adiciona a avaliação em uma lista de avaliações
        '''
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacoes(self):
        '''
        Faz a media das avaliações de um restaurante
        '''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)


    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, '_tamanho'):
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)
            elif hasattr(item, 'tipo'):
                mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tipo: {item.tipo} | Tamanho: {item.tamanho}'
                print(mensagem_sobremesa)




