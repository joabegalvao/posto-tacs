#!/usr/bin/env python3
"""Gera as imagens otimizadas da landing page a partir dos arquivos originais.

Uso (na raiz do projeto):
    python3 tools/optimize-images.py

Requer Pillow (pip install pillow) e a pasta materiais-de-origem/. Os
originais nunca são alterados. Para trocar uma foto, substitua o arquivo de
origem ou edite a lista PHOTOS e rode o script novamente.
"""
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "materiais-de-origem"
SRC = SOURCES / "fotos"
AVATAR_SRC = SOURCES / "avaliacoes"
LOGO_SRC = SOURCES / "logo" / "Posto Tacs logo.png"
OUT = ROOT / "assets" / "img"

# As fotos recebidas têm de 360 a 715 px de largura. Nada é ampliado: a maior
# versão gerada é a do tamanho original.
WIDTHS = (360, 520)
LOGO_BLUE = (0, 62, 128)   # #003E80, fundo do logo
NIGHT = (6, 13, 26)        # #060D1A, fundo escuro da página

# nome de saída -> arquivo em materiais-de-origem/fotos
PHOTOS = {
    "posto-a-noite": "Screenshot 2026-09-29 102027.png",
    "bomba-de-combustivel": "Screenshot 2026-09-29 101826.png",
    "fachada-tacs-go": "Screenshot 2026-09-29 101849.png",
    "deck-com-mesas": "Screenshot 2026-09-29 102108.png",
    "interior-da-conveniencia": "Screenshot 2026-09-29 102054.png",
}

# Fotos de perfil: nome de saída -> arquivo em materiais-de-origem/avaliacoes
AVATARS = {
    "avaliacao-thiago-pacheco": "Thiago_Pacheco.png",
    "avaliacao-jessica-cristina": "Jessica_Cristina.png",
    "avaliacao-marcos-goncalves": "Marcos Gonçalves.png",
}

# Recorte aplicado a todas as fotos (esquerda, topo, direita, base), em pixels.
# As capturas de tela trazem uma linha irregular nas bordas.
TRIM = (2, 2, 2, 2)

# Recortes extras por arquivo, somados ao TRIM. Eles retiram textos e marcas
# aplicados sobre as fotos nas artes do Instagram.
CROPS = {
    # arte em carrossel: fica só a bomba, sem o cartão de texto à esquerda
    # nem a faixa de texto da base
    "Screenshot 2026-09-29 101826.png": (452, 0, 0, 44),
    # assinatura do posto aplicada na base da foto
    "Screenshot 2026-09-29 101849.png": (0, 0, 0, 96),
}


def open_source(source: str) -> Image.Image:
    im = Image.open(SRC / source).convert("RGB")
    extra = CROPS.get(source, (0, 0, 0, 0))
    left, top, right, bottom = (a + b for a, b in zip(TRIM, extra))
    return im.crop((left, top, im.width - right, im.height - bottom))


def resize_to_width(im: Image.Image, width: int) -> Image.Image:
    if im.width <= width:
        return im.copy()
    height = round(im.height * width / im.width)
    return im.resize((width, height), Image.LANCZOS)


def build_photos() -> None:
    for name, source in PHOTOS.items():
        im = open_source(source)
        for width in WIDTHS:
            if width < im.width:
                resize_to_width(im, width).save(
                    OUT / f"{name}-{width}.webp", "WEBP", quality=80, method=6
                )
        im.save(OUT / f"{name}-{im.width}.webp", "WEBP", quality=80, method=6)
        # fallback JPEG para navegadores sem WebP
        im.save(
            OUT / f"{name}-{im.width}.jpg", "JPEG", quality=82, optimize=True, progressive=True
        )
        print(f"{name}: {im.width}x{im.height}")


def build_logo() -> None:
    """O logo original tem 400x400 px: o "P" branco sobre um quadrado azul.
    Nada é redesenhado. O script só uniformiza o azul do fundo, que tinha
    pequenas variações de compressão, e gera os tamanhos usados na página."""
    logo = Image.open(LOGO_SRC).convert("RGB")
    pixels = logo.load()
    for y in range(logo.height):
        for x in range(logo.width):
            r, g, b = pixels[x, y]
            if abs(r - LOGO_BLUE[0]) + abs(g - LOGO_BLUE[1]) + abs(b - LOGO_BLUE[2]) <= 24:
                pixels[x, y] = LOGO_BLUE

    for width in (400, 144):
        out = logo if width == logo.width else logo.resize((width, width), Image.LANCZOS)
        out.save(OUT / f"logo-posto-tacs-{width}.png", optimize=True)
        out.save(OUT / f"logo-posto-tacs-{width}.webp", "WEBP", quality=94, method=6)
    print(f"logo-posto-tacs: {logo.width}x{logo.height}")

    # Ícones
    for name, size in (("favicon-32", 32), ("apple-touch-icon", 180), ("icon-192", 192)):
        logo.resize((size, size), Image.LANCZOS).save(OUT / f"{name}.png", optimize=True)


def build_avatars() -> None:
    """Mantém o tamanho e a transparência originais (72x72 px)."""
    for name, source in AVATARS.items():
        im = Image.open(AVATAR_SRC / source).convert("RGBA")
        im.save(OUT / f"{name}.png", optimize=True)
        im.save(OUT / f"{name}.webp", "WEBP", quality=90, method=6)
        print(f"{name}: {im.width}x{im.height}")


def build_social_card() -> None:
    """Imagem de compartilhamento (1200x630): logo à esquerda e foto à direita,
    sem ampliar a foto além do necessário."""
    card = Image.new("RGB", (1200, 630), NIGHT)

    photo = open_source(PHOTOS["posto-a-noite"])
    photo = ImageOps.fit(photo, (600, 630), Image.LANCZOS, centering=(0.5, 0.62))
    card.paste(photo, (600, 0))

    logo = Image.open(OUT / "logo-posto-tacs-400.png").convert("RGB").resize((300, 300), Image.LANCZOS)
    card.paste(logo, ((600 - 300) // 2, (630 - 300) // 2))

    card.save(OUT / "compartilhamento.jpg", "JPEG", quality=86, optimize=True, progressive=True)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_photos()
    build_logo()
    build_avatars()
    build_social_card()
    total = sum(f.stat().st_size for f in OUT.iterdir())
    print(f"{len(list(OUT.iterdir()))} arquivos, {total / 1024:.0f} KB no total")
