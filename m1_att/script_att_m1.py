import cv2

# Script que abre um video em formato mp4, conta quantos quadros tem e salva o quadro do meio

#caminho para pegar o video na maquina e fazer a analise e corte
caminho = ""
cap = cv2.VideoCapture(caminho)
quadros = []

while True:
    ret, quadro = cap.read()
    if not ret:
        break
    quadros.append(quadro)


# propriedades do video
print("Propriedades do vídeo:")
print(f"  Largura: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}")
print(f"  Altura: {int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
print(f"  FPS: {cap.get(cv2.CAP_PROP_FPS)}")
# print(f"  Codec: {chr(int(cap.get(cv2.CAP_PROP_FOURCC) & 0xFF))}{chr(int(cap.get(cv2.CAP_PROP_FOURCC) >> 8 & 0xFF))}{chr(int(cap.get(cv2.CAP_PROP_FOURCC) >> 16 & 0xFF))}{chr(int(cap.get(cv2.CAP_PROP_FOURCC) >> 24 & 0xFF))}")
print(f"  Contagem de quadros (estimada pelo codec): {int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}")

cap.release()

quadro_do_meio = len(quadros) // 2

cv2.imwrite('Quadro_do_meio.jpg', quadros[quadro_do_meio])

print(f'Total dos quadros no video: {len(quadros)}')