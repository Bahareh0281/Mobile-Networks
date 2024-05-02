from PIL import Image

def transparent(image_path, watermark_path, position):

    image = Image.open(image_path)
    watermark = Image.open(watermark_path).convert("RGBA")

    # Resize the watermark image to fit the specified position
    watermark = watermark.resize((position[2] - position[0], position[3] - position[1]))

    # Create a transparent layer
    transparent_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Paste the watermark onto the transparent layer at the specified position
    transparent_layer.paste(watermark, position, mask=watermark)

    # Combine the original image with the transparent layer using alpha compositing
    watermarked_image = Image.alpha_composite(image.convert("RGBA"), transparent_layer)

    watermarked_image.save("watermarked_image.png")

# Example usage
image_path = "original_image.jpg"
watermark_path = "IUST.png"
position = (370, 20, 450, 100)

transparent(image_path, watermark_path, position)
