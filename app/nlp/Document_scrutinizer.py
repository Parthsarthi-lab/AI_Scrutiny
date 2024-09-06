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
        self.file_name = file.filename
        self.path = f"uploads/{self.file_name}"
        self.doc = fitz.open(self.path)
        self.page_dimensions = [(page.rect.width, page.rect.height) for page in self.doc]
        self.image_paths = convert_pdf_to_images(file.filename,self.path,"images\\")
        self.processed_image_paths = {}
        
        for count,image_path in enumerate(self.image_paths,start=1):
            processed_image_dir = f"processed_images\\{file.filename}"
            processed_image_name = "processed_" + os.path.basename(image_path)
            self.processed_image_paths[count] = os.path.join(processed_image_dir, processed_image_name)


        
        self.text = {}
        for page_number, image_path in enumerate(self.image_paths, start=1):
            # Load the image for the current page
            #page_image = cv2.imread(image_path)
            
            # Perform OCR to extract text from the image
            self.text[page_number] = ocr_process(image_path,file.filename)
            
        
        self.trigger()
        


    def trigger(self):
        self.common_defects = {}
        self.common_defects["paper_typing_specifications"]=self.paper_typing_spec()
        self.common_defects["language_translation"]=self.language_translation()
        #self.heading_checker()
        #self.adherence_time_limits()
        #self.affidavit_interpretation()

    def paper_typing_spec(self):
        paper_size_errors = paper_size(self)
        pg_numbering_errors = page_numbering(self)
        #font(self) # Cannot be done at the moment
        #font_size(self) # Cannot be done at the moment
        #spacing(self) # Cannot be done at the moment
        #margin(self) # Cannot be done at the moment

        

        #legibility_neatness(self) # Will do later
        if paper_size_errors == {}:
            paper_size_errors = None
        if pg_numbering_errors =={}:
            pg_numbering_errors = None
        return [paper_size_errors,pg_numbering_errors]

    def language_translation(self):
        lang = check_document_language(self)
        lang_translation_error= {}
        if lang!="en":
            availability = check_translated_document_available(self)
            certificate = check_certificate_translation(self)
            #format_check = check_format_translated(self)
            #check_consistency_translation(self)

            if not availability:
                lang_translation_error["Availability of translation"]= {
                "issue": "Translated document not available for non-english text",
                "Rules": "Order VIII Rule 3 - Supreme Court Rules 2013"
                }
            if not certificate:
                lang_translation_error["Oath of translation"]= {
                "issue": "Oath of translation not taken by translator",
                "Rules": "Order VIII Rule 4 - Supreme Court Rules 2013"
                }
            """if False in format_check.values():
                lang_translation_error.append({
                    "issue":"Translated document not in the same format as the orginial document",
                    "Rules":"SC Rules 2013"
                })"""
            if lang_translation_error == {}:
                return None
            else:
                return lang_translation_error
        else:
            return None

        


    """def heading_checker(self):
        check_heading(self)
"""
    """def adherence_time_limits(self):
        check_slp(self)
        check_civil_case(self)
        check_criminal_case(self)
        check_90_days_from_impugned_order(self)
        check_60_days_from_refusal_of_certificate(self)
        check_60_days_from_impugned_order_death_sentence(self)
        check_90_days_from_impugned_order_excluding_death(self)
        check_60_days_from_refusal_of_certificate_fitness(self)"""


    """def affidavit_interpretation(self):
        language = check_deponent_understand_eng()
        if language!="English":
            check_certificate_interpretation(self)"""




