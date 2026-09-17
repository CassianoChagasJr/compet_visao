import cv2
import numpy as np

# --- Seção de Criação de Vídeo ---
# Configurações para a criação do vídeo (FPS, dimensões, nome do arquivo)
fps_criacao = 20
largura_criacao, altura_criacao = 320, 240
nome_arquivo_video_criado = "video_atividade_m1.mp4"

# Define o codec para o vídeo (MP4V)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Inicializa o objeto para escrever o vídeo
escritor = cv2.VideoWriter(
    nome_arquivo_video_criado,
    fourcc,
    fps_criacao,
    (largura_criacao, altura_criacao),
)

# Loop para gerar e adicionar quadros ao vídeo
num_quadros_criacao = 60
for i in range(num_quadros_criacao):
    # Cria um quadro branco
    quadro = np.full((altura_criacao, largura_criacao, 3), 255, dtype=np.uint8)
    # Calcula a posição X do círculo para criar um movimento
    x_pos = int(30 + (largura_criacao - 60) * i / num_quadros_criacao)

    # Desenha um círculo azul no quadro
    cv2.circle(
        quadro,
        (x_pos, altura_criacao // 2),
        20,
        (255, 0, 0),
        thickness=-1,
    )
    # Escreve o quadro no arquivo de vídeo
    escritor.write(quadro)

# Libera o objeto escritor, finalizando a criação do vídeo
escritor.release()
print(f"Vídeo '{nome_arquivo_video_criado}' criado com {num_quadros_criacao} quadros.")

# --- Seção de Análise de Vídeo ---
# Define o caminho do vídeo a ser analisado (pode ser o recém-criado ou um externo)
caminho_video_analise = nome_arquivo_video_criado
# Inicializa o objeto para capturar/ler o vídeo
captura = cv2.VideoCapture(caminho_video_analise)
quadros_lidos = []

# Verifica se o vídeo foi aberto corretamente
if not captura.isOpened():
    print(f"Erro: Não foi possível abrir o vídeo '{caminho_video_analise}'.")
else:
    # Lê todos os quadros do vídeo
    while True:
        ret, quadro_atual = captura.read()
        if not ret:
            break
        quadros_lidos.append(quadro_atual)

    # Exibe as propriedades do vídeo analisado
    print("\nPropriedades do vídeo analisado:")
    print(f"  FPS: {captura.get(cv2.CAP_PROP_FPS)}")
    print(f"  Contagem de quadros: {int(captura.get(cv2.CAP_PROP_FRAME_COUNT))}")

    # Libera o objeto de captura
    captura.release()

    # Se quadros foram lidos, processa e exibe o quadro do meio
    if quadros_lidos:
        # Calcula o índice do quadro do meio
        indice_quadro_meio = len(quadros_lidos) // 2
        nome_arquivo_quadro_meio = 'Quadro_do_meio.jpg'
        # Salva o quadro do meio como imagem
        cv2.imwrite(nome_arquivo_quadro_meio, quadros_lidos[indice_quadro_meio])

        # Carrega e exibe o quadro do meio no Colab
        quadro_meio_para_exibir = cv2.imread(nome_arquivo_quadro_meio)
        print("\nQuadro do meio:")
        cv2_imshow(quadro_meio_para_exibir)
    else:
        print("Nenhum quadro foi lido do vídeo para análise.")

    # Exibe o total de quadros lidos
    print(f'\nTotal de quadros lidos do vídeo: {len(quadros_lidos)}')
