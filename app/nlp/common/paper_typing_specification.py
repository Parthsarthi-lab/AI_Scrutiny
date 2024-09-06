import cv2
import pytesseract
import re

def paper_size(petition):
    """Check if the document is in A4 size."""
    paper_size_errors = {}
    a4_width_points = 595.32
    a4_height_points = 841.92
    tolerance = 1.0  # Allow a small margin for error

    for pg_no,pg_dim in enumerate(petition.page_dimensions,start=1):

        width, height = pg_dim
        defect_check = (abs(width - a4_width_points) <= tolerance) and (abs(height - a4_height_points) <= tolerance)

        if not defect_check:
            paper_size_errors[pg_no]= {
            "page": pg_no,
            "issue": "The document is not in A4 size paper.",
            "rule": "Supreme Court Circular dated 05th March 2020 (F.No. 01/Judl./2020)"
        }
    return paper_size_errors


def font():
    pass

def font_size():
    pass

def spacing():
    pass

def margin():
    pass

def page_numbering(document):
    """Detect the page number on the page using OCR."""
    pg_numbering_errors=  {}
    # Assuming that the page number is at the bottom right of the page
    # Crop the bottom part of the page to find the page number
    for page_number, image_path in enumerate(document.image_paths, start=1):
        # Load the image for the current page
        page_image = cv2.imread(image_path)
        height, width = page_image.shape[:2]
        cropped_image = page_image[int(height*0.9):height, int(width*0.7):width]

        # Use OCR to detect text in the cropped area
        ocr_data = pytesseract.image_to_string(cropped_image, config='--psm 6').strip()
         # Extract only the numeric portion of the OCR result
        numeric_match = re.search(r'\d+', ocr_data)
        
        if numeric_match:
            detected_page_number = int(numeric_match.group(0))
            # Compare the detected page number with the expected page number
            if detected_page_number != page_number:
                pg_numbering_errors[page_number] = {
                    "page": page_number,
                    "issue": f"Page numbering is incorrect. Detected: {detected_page_number}, Expected: {page_number}.",
                    "rule": "Supreme Court Formatting Guidelines"
                }
        else:
            pg_numbering_errors[page_number] = {
                "page": page_number,
                "issue": "Page number not detected or not readable.",
                "rule": "Supreme Court Formatting Guidelines"
            }
            
    return pg_numbering_errors

def legibility_neatness():
    pass