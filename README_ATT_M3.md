# Atividade - M3 - Entrega

O arquivo `keypoints.json` foi gerado a partir de `att_m2.mp4` (vídeo do M2) com o comando:

```bash
python -m extract.py --input att_m2.mp4 --output keypoints.json
```

## Estrutura do `keypoints.json`

### 1. `metadata`
Informações sobre o vídeo e a extração:
- `video_id`: `aafad2cf-9aa2-41d4-9960-4608628da92c`
- `source_file`: `att_m2.mp4`
- `fps`: **60,06**
- `frames_declared`: **980**
- `frames_processed`: **980**
- `hand_detection_rate`: taxa de detecção de mãos (**55,41%**)
- `pose_detection_rate`: taxa de detecção de pose (**100%**)
- `config`: parâmetros usados na extração
  - `max_hands`: 2
  - `detect_pose`: true
  - `min_detection_confidence`: 0.5
  - `min_tracking_confidence`: 0.5

### 2. `frames`
Lista com um item por quadro do vídeo. Cada item contém:
- `hands`: até duas mãos, cada uma com os **21 landmarks** normalizados (0 a 1)
- `pose`: os **33 landmarks** do corpo

### 3. Landmarks
Cada landmark segue o formato:

```json
{
  "landmark": i,
  "x": 0.0,
  "y": 0.0,
  "z": 0.0,
  "score": 0.0
}
```

- `landmark`: índice `i` do ponto (identifica qual parte do corpo ou da mão ele representa, ex.: pulso, cotovelo, ponta do dedo)
- `x`, `y`: coordenadas do ponto no quadro, normalizadas entre 0 e 1
- `z`: profundidade relativa do ponto (também normalizada), indicando o quão próximo ou distante ele está da câmera em relação a um ponto de referência
- `score`: confiança de detecção (mão) ou visibilidade do ponto (pose)

> **Nota:** os valores acima são apenas ilustrativos. No arquivo `keypoints.json` real, cada landmark aparece com valores numéricos diferentes destes, correspondentes às coordenadas efetivamente detectadas em cada quadro do vídeo.