import cv2


# Script que abre um video em formato mp4, conta quantos quadros tem e salva o quadro do meio

cap = cv2.VideoCapture()
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

