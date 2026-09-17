import cv2

# Script que abre um video em formato mp4, conta quantos quadros tem e salva o quadro do meio

cap = cv2.VideoCapture("Caminho para o vídeo .mp4") #caminho para pegar o video na maquina e fazer a analise e corte
quadros = []

while True:
    ret, quadro = cap.read()
    if not ret:
        break
    quadros.append(quadro)

cap.release()

quadro_do_meio = len(quadros) // 2

cv2.imwrite('Quadro_do_meio.jpg', quadros[quadro_do_meio])

print('Total dos quadros no video: ', len(quadro))

