import os
from PIL import Image, ImageDraw, ImageFont


def generate_certificate(thread_count, density_score, level):

    os.makedirs("certificates", exist_ok=True)

    width = 1000
    height = 700

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 55)
        subtitle_font = ImageFont.truetype("arial.ttf", 30)
        text_font = ImageFont.truetype("arial.ttf", 26)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    # Border
    draw.rectangle(
        (20, 20, width - 20, height - 20),
        outline="black",
        width=6
    )

    # Title
    title = "🕷 COBWEB CONSTRUCTION CERTIFICATE 🕸"

    draw.text(
        (width // 2, 100),
        title,
        fill="black",
        font=title_font,
        anchor="mm"
    )

    draw.text(
        (width // 2, 180),
        "Officially Certified by the Department of Unnecessary Technology",
        fill="black",
        font=subtitle_font,
        anchor="mm"
    )

    draw.text(
        (width // 2, 280),
        f"VISIBLE THREADS: {thread_count}",
        fill="black",
        font=text_font,
        anchor="mm"
    )

    draw.text(
        (width // 2, 330),
        f"DENSITY SCORE: {density_score}%",
        fill="black",
        font=text_font,
        anchor="mm"
    )

    draw.text(
        (width // 2, 380),
        f"COBWEB LEVEL: {level}",
        fill="black",
        font=text_font,
        anchor="mm"
    )

    # Funny comments
    comments = {
        "LOW": "Construction status: The spider is still looking for an architect.",
        "MODERATE": "Construction status: Work in progress. Spider approved.",
        "HIGH": "Construction status: Serious spider engineering detected!",
        "VERY HIGH": "Construction status: The spider has clearly hired a contractor!",
        "LEGENDARY": "Construction status: Five-star spider architecture!"
    }

    comment = comments.get(
        level,
        "Construction status: Definitely made by a professional spider."
    )

    draw.text(
        (width // 2, 470),
        comment,
        fill="black",
        font=text_font,
        anchor="mm"
    )

    draw.text(
        (width // 2, 570),
        "CERTIFIED COBWEB ENGINEERING SYSTEM",
        fill="black",
        font=subtitle_font,
        anchor="mm"
    )

    output_path = "certificates/cobweb_certificate.png"

    image.save(output_path)

    return output_path