import fitz
import cv2
from ..utils.pdf_handler import convert_pdf_to_images
from ..ocr.ocr import ocr_process
from ..nlp.common.paper_typing_specification import *
from ..nlp.common.language_translation import *
from ..nlp.common.heading_checker import *
from ..nlp.common.adherence_limits import *
from ..nlp.common.affidavit_interpretation import *

class Document:
    def __init__(self,file):

        # File metadata
        self.path = f"uploads/{file.filename}"
        """self.doc = fitz.open(self.path)
        self.page_dimensions = [(page.rect.width, page.rect.height) for page in self.doc]"""

        self.trigger()

        """self.image_paths = convert_pdf_to_images(self.path)
        defects_by_page = {}

        for page_number, image_path in enumerate(self.image_paths, start=1):
            # Load the image for the current page
            page_image = cv2.imread(image_path)
            
            # Perform OCR to extract text from the image
            text = ocr_process(image_path)"""


    def trigger(self):
        self.paper_typing_spec()
        self.language_translation()
        self.heading_checker()
        self.adherence_time_limits()
        self.affidavit_interpretation()

    def paper_typing_spec(self):
        paper_size(self)
        font(self)
        font_size(self)
        spacing(self)
        margin(self)
        page_numbering(self)
        legibility_neatness(self)

    def language_translation(self):
        lang = check_document_language(self)
        if lang!="English":
            check_translated_document_available(self)
            check_certificate_translation(self)
            check_format_translated(self)
            check_consistency_translation(self)
        else:
            pass



    def heading_checker(self):
        check_heading(self)

    def adherence_time_limits(self):
        check_slp(self)
        check_civil_case(self)
        check_criminal_case(self)
        check_90_days_from_impugned_order(self)
        check_60_days_from_refusal_of_certificate(self)
        check_60_days_from_impugned_order_death_sentence(self)
        check_90_days_from_impugned_order_excluding_death(self)
        check_60_days_from_refusal_of_certificate_fitness(self)


    def affidavit_interpretation(self):
        language = check_deponent_understand_eng()
        if language!="English":
            check_certificate_interpretation(self)




