from pdf2image import convert_from_path
import os

def convert_pdf_to_images(filename,pdf_path, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(f"{output_dir}\\{filename}"):
        os.makedirs(f"{output_dir}\\{filename}")


    pages = convert_from_path(pdf_path)
    image_paths = []
    for i, page in enumerate(pages):
        image_path = os.path.join(output_dir, filename,f"page_{i + 1}.png")
        page.save(image_path, 'PNG')
        image_paths.append(image_path)
    return image_paths