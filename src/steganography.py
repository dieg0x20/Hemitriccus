from PIL import Image
import os
import click


@click.group()
def cli():
    pass

def message_to_bin(message):
    print("Mensagem binária: ", ''.join(format(ord(char), '08b') for char in message))
    return ''.join(format(ord(char), '08b') for char in message)

@cli.command()
@click.option('--message', prompt='Mensagem que deseja encriptar', help='Escreva a mensagem que deseja encriptar')
@click.option('--image', '-i', prompt='Imagem que será modificada', help='Caminho da imagem para ocultar a mensagem')
def encode_message(message, image):
    output_image_path = os.path.join(os.getcwd(), 'encoded_image.png')

    # Abre a imagem
    img = Image.open(image)
    img = img.convert('RGB')
    pixels = img.load()

    # Converte a mensagem em binário e adiciona o delimitador
    bin_message = ''.join(format(ord(char), '08b') for char in message) + '11111111'
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
                pixels[x, y] = (r, g, b)
                idx += 1
            else:
                img.save(output_image_path)
                click.echo(f"Mensagem escondida e salva no {output_image_path}")
                return

    click.echo(f"Mensagem escondida e salva no {output_image_path}")



@cli.command()
@click.option('--image', '-i', prompt='Imagem que será modificada', help='Caminho da imagem para ocultar a mensagem')
def decode_message(image):
        img = Image.open(image)
        img = img.convert('RGB')
        pixels = img.load()

        width, height = img.size
        bin_message = ''

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                bin_message += format(r, '08b')[-1]  #pega o ultimo bit significativo

                if bin_message[-8:]== '11111111' and len(bin_message)%8==0 :  
                   decoded_message = bin_to_message(bin_message[:-8])
                   click.echo(f"Mensagem decodificada: {decoded_message}")
                   return decode_message
    
        return "Nenhuma menssage encontrada"

def bin_to_message(binary_message):
    # Converte a mensagem binária para texto
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

cli.add_command(encode_message)
cli.add_command(decode_message)

#def main():
    #image_path = input("Digite o caminho da imagem: ")

    #if not os.path.exists(image_path):
    #    print("Imagem não encontrada.")
    #    return

    #secret_message = input("Digite a mensagem secreta que deseja esconder: ")

    # Define o caminho de saída da imagem modificada
    #output_image_path = os.path.join(os.getcwd(), 'encoded_image.png')

    # Codifica a mensagem na imagem
    #encode_result = encode_message(image_path, secret_message, output_image_path)
    #print(encode_result)

    #decodificar a imagem
    #decoded_message = decode_message(output_image_path)
    #print("A mensagem decodificada: ", decoded_message)
if __name__ == "__main__":
    cli()
