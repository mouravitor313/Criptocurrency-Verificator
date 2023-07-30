# CriptoChecker

CriptoChecker é um script em Python que usa a API do CoinGecko para obter informações sobre criptomoedas. Ele permite que você verifique o preço atual e o histórico de preços de uma criptomoeda específica, bem como veja a lista de criptomoedas suportadas pela API do CoinGecko.

## Requisitos

Para executar o CriptoChecker, você precisará ter o Python 3.x instalado em seu computador. Além disso, você precisará instalar as seguintes bibliotecas:

- PySimpleGUI
- requests

Você pode instalar essas bibliotecas executando os seguintes comandos no terminal:

```
pip install pysimplegui
pip install requests
```

## Como usar

Para usar o CriptoChecker, basta executar o script `criptochecker.py` usando o Python. Isso abrirá uma janela com a interface gráfica do programa.

Na janela principal, você pode digitar o ID da criptomoeda que deseja verificar (por exemplo, "bitcoin") e a moeda de conversão desejada (por exemplo, "usd") nas entradas de texto correspondentes. Em seguida, clique no botão "Verificar" para verificar o preço e o histórico de preços da criptomoeda escolhida.

Você também pode clicar no botão "Mostrar Criptomoedas Suportadas" para mostrar a lista de criptomoedas suportadas pela API do CoinGecko na mesma janela.

## Licença

CriptoChecker é um software livre e de código aberto licenciado sob a [Licença MIT](LICENSE).
