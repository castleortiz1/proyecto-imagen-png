from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Define las dimensiones de la imagen y el color de fondo
IMAGE_SIZE = (800, 600)
BG_COLOR = (0, 0, 0)  # negro

# Crea una nueva imagen y un contexto de dibujo
image = Image.new("RGB", IMAGE_SIZE, BG_COLOR)
draw = ImageDraw.Draw(image)

# Define el texto y sus propiedades
TEXT = "Cyberpunk"
TEXT_POSITION = (50, 50)
TEXT_COLOR = (255, 0, 0)  # rojo
# Ruta correcta a la fuente TrueType
FONT_PATH = os.path.join(os.path.dirname(__file__), '..', 'fonts', 'Roboto-Black.ttf')
FONT_SIZE = 100

# Verifica si la ruta de la fuente existe
if not os.path.exists(FONT_PATH):
    raise FileNotFoundError(f"La fuente no se encontró en la ruta: {FONT_PATH}")

# Carga la fuente
try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
except IOError:
    raise IOError(f"No se pudo cargar la fuente desde la ruta: {FONT_PATH}")

# Dibuja el texto
draw.text(TEXT_POSITION, TEXT, fill=TEXT_COLOR, font=font)

# Define los colores neon
NEON_PINK = (255, 20, 147)  # rosa neón
NEON_BLUE = (0, 255, 255)  # azul neón

# Dibuja algunas líneas neon verticales
for i in range(0, IMAGE_SIZE[0], 20):
    draw.line([(i, 0), (i, IMAGE_SIZE[1])], fill=NEON_PINK, width=1)

# Dibuja algunas líneas neon horizontales
for i in range(0, IMAGE_SIZE[1], 20):
    draw.line([(0, i), (IMAGE_SIZE[0], i)], fill=NEON_BLUE, width=1)

# Aplica un efecto de desenfoque para darle un estilo cyberpunk
image = image.filter(ImageFilter.GaussianBlur(2))

# Define la ruta de salida y verifica si la carpeta de salida existe
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output')
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

OUTPUT_PATH = os.path.join(OUTPUT_DIR, "cyberpunk_style_image.png")

# Guarda la imagen en un archivo
try:
    image.save(OUTPUT_PATH)
    print(f"Imagen guardada en: {OUTPUT_PATH}")
except IOError:
    raise IOError(f"No se pudo guardar la imagen en la ruta: {OUTPUT_PATH}")
