# Hemitriccus

## Esteganografia LSB em Imagens

Este projeto implementa a técnica de **Esteganografia LSB (Least Significant Bit)** para esconder e revelar mensagens dentro de imagens. A esteganografia LSB é uma técnica que modifica o bit menos significativo (LSB) de cada componente de cor de um pixel em uma imagem, permitindo armazenar dados sem afetar significativamente a aparência da imagem.

## Como Funciona

1. **Esconder a Mensagem:** A função `encode_message` pega uma mensagem de texto fornecida pelo usuário e a converte para seu formato binário. Em seguida, ela altera o último bit do valor RGB de cada pixel da imagem para armazenar a mensagem binária.
   
2. **Revelar a Mensagem:** A função `decode_message` examina os últimos bits dos valores RGB de cada pixel da imagem modificada e recupera a mensagem oculta.

## Requisitos

Antes de rodar o código, certifique-se de ter o Python instalado em sua máquina. Além disso, você precisará instalar a biblioteca Pillow, que é usada para manipulação de imagens. Você pode instalar essa dependência com o seguinte comando:

```bash
pip install click
pip install Pillow
```

ou

```bash
pip install requirements.txt
```

## Como Usar

### 1. Codificar uma Mensagem

Para esconder uma mensagem dentro de uma imagem, use o comando:

```bash
python steganography.py encode-message --message "Sua mensagem secreta" --image caminho/para/imagem.jpg
```

- **--message**: A mensagem que você deseja esconder.
- **--image**: O caminho para a imagem onde a mensagem será escondida.

Isso irá gerar uma imagem chamada `encoded_image.png` no diretório atual, que contém a mensagem secreta oculta.

### 2. Decodificar a Mensagem

Para recuperar a mensagem oculta de uma imagem, use o comando:

```bash
python steganography.py decode-message --image caminho/para/encoded_image.png
```

- **--image**: O caminho para a imagem que contém a mensagem oculta.

A mensagem secreta será exibida no terminal.


## Detalhes Técnicos

A técnica de **esteganografia LSB** (Least Significant Bit) modifica os bits menos significativos dos valores RGB dos pixels da imagem para armazenar a mensagem binária. Isso é feito de forma que a alteração nos valores das cores é tão pequena que não é perceptível a olho nu.

### Exemplo de como funciona:

- Se um valor de cor RGB for `R: 10101000`, `G: 11001010`, `B: 11110011` (em binário), a alteração do último bit de cada valor (LSB) pode representar um único bit da mensagem.
- Se a mensagem binária for `11001010 10101010`, os bits menos significativos serão modificados para esconder esses valores sem alterar de forma visível a imagem.


## Fontes

- [Hacking na Web - Esteganografia por LSB](https://hackingnaweb.com/criptografia/esteganografia-por-lsb/)


