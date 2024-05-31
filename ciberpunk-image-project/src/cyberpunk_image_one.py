from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Define las dimensiones de la imagen y el color de fondo
IMAGE_SIZE = (800, 600)
BG_COLOR = (0, 0, 0)  # negro
FONT_SIZE = 100

# Función para centralizar el texto
def get_centered_position(draw, text, font, image_size):
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2
    return x, y

# Función para crear una imagen con un estilo específico
def create_image(style):
    # Ruta a la fuente TrueType
    FONT_PATH = os.path.join(os.path.dirname(__file__), '..', 'fonts', 'Roboto-Black.ttf')
    
    # Verifica si la ruta de la fuente existe
    if not os.path.exists(FONT_PATH):
        raise FileNotFoundError(f"La fuente no se encontró en la ruta: {FONT_PATH}")

    # Carga la fuente
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        raise IOError(f"No se pudo cargar la fuente desde la ruta: {FONT_PATH}")

    # Crea una nueva imagen y un contexto de dibujo
    image = Image.new("RGB", IMAGE_SIZE, BG_COLOR)
    draw = ImageDraw.Draw(image)

    # Define el texto y sus propiedades
    TEXT = "Cyberpunk"
    
    # Centraliza el texto
    text_position = get_centered_position(draw, TEXT, font, IMAGE_SIZE)
    
    if style == 'cyberpunk':
        TEXT_COLOR = (255, 0, 0)  # rojo
        draw.text(text_position, TEXT, fill=TEXT_COLOR, font=font)
        NEON_PINK = (255, 20, 147)  # rosa neón
        NEON_BLUE = (0, 255, 255)  # azul neón

        # Dibuja algunas líneas neon
        for i in range(0, IMAGE_SIZE[0], 20):
            draw.line([(i, 0), (i, IMAGE_SIZE[1])], fill=NEON_PINK, width=1)
        for i in range(0, IMAGE_SIZE[1], 20):
            draw.line([(0, i), (IMAGE_SIZE[0], i)], fill=NEON_BLUE, width=1)

        # Aplica un efecto de desenfoque para darle un estilo cyberpunk
        image = image.filter(ImageFilter.GaussianBlur(2))

    elif style == 'matrix':
        TEXT_COLOR = (0, 255, 0)  # verde
        BG_COLOR_MATRIX = (0, 0, 0)  # negro
        image = Image.new("RGB", IMAGE_SIZE, BG_COLOR_MATRIX)
        draw = ImageDraw.Draw(image)
        draw.text(text_position, TEXT, fill=TEXT_COLOR, font=font)

    elif style == 'gothic':
        TEXT_COLOR = (255, 255, 255)  # blanco
        BG_COLOR_GOTHIC = (0, 0, 0)  # negro
        image = Image.new("RGB", IMAGE_SIZE, BG_COLOR_GOTHIC)
        draw = ImageDraw.Draw(image)
        draw.text(text_position, TEXT, fill=TEXT_COLOR, font=font)

    # Define la ruta de salida y verifica si la carpeta de salida existe
    OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output')
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    OUTPUT_PATH = os.path.join(OUTPUT_DIR, f"{style}_style_image.png")

    # Guarda la imagen en un archivo
    try:
        image.save(OUTPUT_PATH)
        print(f"Imagen guardada en: {OUTPUT_PATH}")
    except IOError:
        raise IOError(f"No se pudo guardar la imagen en la ruta: {OUTPUT_PATH}")

# Crear imágenes con diferentes estilos
create_image('cyberpunk')
create_image('matrix')
create_image('gothic')
