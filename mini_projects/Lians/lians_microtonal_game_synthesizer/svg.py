from wand.api import library
import wand.color
import wand.image
from defines import (
    BATTLESHIP_GREY,
    FLORAL_WHITE,
    GRAY,
    DIAMOND,
    LIGHT_GRAY_CH,
    BRINK_PINK,
    SHAMROCK_GREEN,
    PINK,
)


def setup_img():
    w_h     = [(140, 256), (140, 240),  (93, 114)]
    sprites = ["diatonic", "chromatic", "microtonal"]
    
    names         = ["regular", "right", "wrong", "not_used"]
    colors_fill   = [FLORAL_WHITE, DIAMOND, PINK, LIGHT_GRAY_CH]
    colors_stroke = [GRAY, SHAMROCK_GREEN, BRINK_PINK, BATTLESHIP_GREY]
    
    for s, wh in zip(sprites, w_h):
        width, height = wh
        for name, cf, cs in zip(names, colors_fill, colors_stroke):
            name_n = f"{s}_{name}"
            svg2png(width, height, name_n, cf, cs)
                

def create_rounded_rectangle_svg(x=0, y=0,\
                                width=140, height=260,\
                                rx=44, ry=54,\
                                fill_color=FLORAL_WHITE,\
                                stroke_color=GRAY,\
                                stroke_width=2):
    
    width_canvas = width + x + (stroke_width * 2)
    height_canvas = height + y + (stroke_width * 2)
    svg_string = f"""
    <svg xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 {width_canvas} {height_canvas}"
        width="{width_canvas}" 
        height="{height_canvas}"
        preserveAspectRatio="xMidYMid meet">
            <rect x="{x + stroke_width}" y="{y + stroke_width}" 
                width="{width}" height="{height}" 
                rx="{rx}" ry="{ry}" 
                fill="rgb{fill_color}" 
                stroke="rgb{stroke_color}" 
                stroke-width="{stroke_width}"
            />
    </svg>
    """
    return svg_string


def svg2png(w, h, n, fc, sc):
    svg_output = create_rounded_rectangle_svg(width=w, height=h, fill_color=fc, stroke_color=sc)
    output_filename = f"{n}.png" 
        
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(svg_output) 
       
    with open(output_filename, "rb") as file:    
        with wand.image.Image() as image:
            with wand.color.Color('transparent') as background_color:
                library.MagickSetBackgroundColor(image.wand, 
                                                background_color.resource) 
            image.read(blob=file.read(), format="svg")
            png_image = image.make_blob("png32")

        with open(output_filename, "wb") as out:
            out.write(png_image)


if __name__ == "__main__":
    setup_img()