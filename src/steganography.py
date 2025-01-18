# Author -> dieg0x20
# Script de esteganografia em python usando a tecnica de LSB
# Instale os requerimentos necessarios para rodar o arquivo com o camando pip install requirements.txt
from PIL import Image
import os

# Converte a mensagem em binário
def message_to_bin(message):
    print("Mensagem binária: ", ''.join(format(ord(char), '08b') for char in message))
    return ''.join(format(ord(char), '08b') for char in message)

# Converte o binário de volta para a mensagem
def bin_to_message(binary_message):
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

# Esconde a mensagem dentro da imagem
def encode_message(image_path, message, output_image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()  # Corrigido o nome da variável

    bin_message = message_to_bin(message) + '11111111'  # Adiciona um delimitador
    print("Mensagem binária: ", bin_message)
    message_len = len(bin_message)
    width, height = img.size
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx < message_len:
                r, g, b = pixels[x, y]
                r_bin = format(r, '08b')
                r_bin = r_bin[:7] + bin_message[idx]  # Substitui o último bit
                r = int(r_bin, 2)
                pixels[x, y] = (r, g, b)  # Atualiza o pixel com o valor modificado
                idx += 1
            else:
                img.save(output_image_path)  # Salva a imagem modificada
                return f"Mensagem escondida e salva no {output_image_path}"

def decode_message(image_path):
        img = Image.open(image_path)
        img = img.convert('RGB')
        pixels = img.load()

        width, height = img.size
        bin_message = ''

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                bin_message += format(r, '08b')[-1]  #pega o ultimo bit significativo

                if bin_message[-8:]== '11111111' and len(bin_message)%8==0 :
                    return bin_to_message(bin_message[:-8])

        return "Nenhuma menssage encontrada"

def main():
    image_path = input("Digite o caminho da imagem: ")

    if not os.path.exists(image_path):
        print("Imagem não encontrada.")
        return

    secret_message = input("Digite a mensagem secreta que deseja esconder: ")

    # Define o caminho de saída da imagem modificada
    output_image_path = os.path.join(os.getcwd(), 'encoded_image.png')

    # Codifica a mensagem na imagem
    encode_result = encode_message(image_path, secret_message, output_image_path)
    print(encode_result)

    #decodificar a imagem
    decoded_message = decode_message(output_image_path)
    print("A mensagem decodificada: ", decoded_message)

if __name__ == "__main__":
    main()
