import cv2

# Script que abre um video em formato mp4, conta quantos quadros tem e salva a imagem do quadro do meio, imprimi

# trecho para criação do video
fps = 20                            # quadros por segundo do vídeo
largura_quadro, altura_quadro = 320, 240      # tamanho de cada quadro (largura, altura)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

escritor = cv2.VideoWriter(
    "video_atividade_m1.mp4",            # arquivo de saída
    fourcc,                         # codec definido acima
    fps,                            # taxa de quadros por segundo
    (largura_v, altura_v),          # frameSize
)

n_quadros = 60                     # quadros a gerar
for i in range(n_quadros):          
    quadro = np.full((altura_v, largura_v, 3), 255, dtype=np.uint8)   # fundo branco
    # x avança um pouco a cada quadro -> dá a sensação de movimento
    x = int(30 + (largura_v - 60) * i / n_quadros)
    cv2.circle(
        quadro,
        (x, altura_v // 2),         # center: (x que avança, meio da altura)
        20,                       
        (255, 0, 0),              # color BGR: azul
        thickness=-1,               # preenchido
    )
    escritor.write(quadro)          # grava este quadro no arquivo de vídeo

escritor.release()                  # fecha o arquivo
print(f"Vídeo criado com {n_quadros} quadros.")

#caminho para pegar o video na maquina e fazer a analise e corte
caminho = "video_atividade_m1.mp4"
cap = cv2.VideoCapture(caminho)
quadros = []

while True:
    ret, quadro = cap.read()
    if not ret:
        break
    quadros.append(quadro)


# propriedades do video
print("Propriedades do vídeo:")
print(f"  FPS: {cap.get(cv2.CAP_PROP_FPS)}")
print(f"  Contagem de quadros: {int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}")

cap.release()

quadro_do_meio = len(quadros) // 2
# Salvando a imagem do quadro do meio
cv2.imwrite('Quadro_do_meio.jpg', quadros[quadro_do_meio])
# Carrega a imagem do quadro do meio
quadro_meio_img = cv2.imread('Quadro_do_meio.jpg')

# Exibe o quadro do meio
print("Quadro do meio:")
cv2_imshow(quadro_meio_img)

print(f'Total dos quadros no video: {len(quadros)}')