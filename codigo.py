from PIL import Image
import os

entrada = "fotogithub.png"      # nome da sua imagem
saida = "fotogithub_menor.jpg"  # nome da nova imagem

img = Image.open(entrada).convert("RGB")

qualidade = 95

while True:
    img.save(saida, "JPEG", quality=qualidade, optimize=True)
    
    tamanho = os.path.getsize(saida)
    
    if tamanho < 1000000:  # 1MB
        break
    
    qualidade -= 5

print("Imagem comprimida com sucesso!")
print("Tamanho final:", tamanho/1024, "KB")