import re
import cv2
import numpy as np
import pytesseract
from PIL import Image

def check_heading_and_filing(affidavit):
    """
    Ensure that the affidavit is headed "In the Supreme Court of India" and filed in the cause, appeal, or matter for which it is sworn.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the heading and filing requirements are met.
    """
    text = affidavit.text[1].lower()

    if "In the Supreme Court of India" in text:
        return {}
    else:
        return {"issue":"Affidavit does not read 'In the Supreme Court of India",
                "rule":"Chapter IX Affidavits Rule 2 -  Handbook on Practice and Procedure and Office Procedure"}


def check_structure_content(affidavit):
    """
    Verify that the affidavit is written in the first person, divided into consecutively numbered paragraphs, and includes the deponent’s description, occupation (if any), and true place of abode.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the structure and content of the affidavit meet the requirements.
    """
     # Define a list of first-person pronouns
    first_person_pronouns = ["i", "my", "me", "mine", "we", "our", "us", "ours"]

    # Convert text to lowercase to ensure case-insensitive matching
    text = ""
    for new in affidavit.text.values():
        text += new
    text = text.lower()

    # Search for first-person pronouns in the text
    for pronoun in first_person_pronouns:
        if re.search(r'\b' + pronoun + r'\b', text):
            return {}
    
    return {"issue":"Affidavit is not in first-person",
            "rule":"Chapter IX Affidavits Rule 3 -  Handbook on Practice and Procedure and Office Procedure"}


"""def check_pardahnashin_ladies(affidavit):
    ""
    For deponents who are pardahnashin ladies, ensure the affidavit is affirmed or sworn before a lady Registrar or Oath Commissioner, and the deponent is identified by someone who knows her, with the identification proved by a separate affidavit.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the requirements for pardahnashin ladies are met.
    ""
    pass
"""
def check_language_and_interpretation(affidavit):
    """
    If the affidavit requires interpretation, verify that it is interpreted by a court-approved interpreter within Delhi.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the language and interpretation requirements are met.
    """
    pass

def check_verification_clause(affidavit):
    """
    In the verification clause, ensure that statements based on personal knowledge are distinguished from those based on information and belief, and that the source of information is disclosed for the latter.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the verification clause is correctly structured.
    """
    pass

def check_corrections(affidavit):
    """
    Ensure that no affidavit contains interlineations, alterations, or erasures unless these are initialed by the authority before whom the affidavit is sworn. Verify that any rewritten words or figures are also initialed.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the corrections are properly initialed.
    """
    pass

def check_exhibit(affidavit):
    """
    Verify that any exhibit annexed to an affidavit is marked with the title and number of the cause, appeal, or matter, and is initialed and dated by the authority before whom it is sworn.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether exhibits are properly marked, initialed, and dated.
    """
    pass

def check_signing_and_swearing(affidavit):
    """
    Ensure that the affidavit is signed and sworn before a Notary, Registrar, or Oath Commissioner as authorized.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the affidavit is properly signed and sworn.
    """

    def preprocess_image(image_path):
        """
        Convert image to grayscale and apply thresholding to enhance signature features.
        """
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, thresh_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
        return thresh_image
    

    def detect_signatures(image_path):
        """
        Detect possible signature regions in the affidavit document.
        
        Parameters:
        image_path (str): The path to the affidavit image.

        Returns:
        list: A list of bounding boxes around detected signature regions.
        """
        # Preprocess the image
        preprocessed_image = preprocess_image(image_path)
        
        # Find contours in the preprocessed image
        contours, _ = cv2.findContours(preprocessed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        signature_boxes = []
        
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            
            # Filter based on aspect ratio and size, assuming signature is a long, narrow region
            if w > h and w > 50 and h > 10:  # Adjust thresholds as needed
                signature_boxes.append((x, y, w, h))
        
        return signature_boxes

    def is_signature_present(image_path):
        """
        Determine if a signature is present in the affidavit document.
        
        Parameters:
        image_path (str): The path to the affidavit image.

        Returns:
        bool: True if a signature is detected, False otherwise.
        """
        signature_boxes = detect_signatures(image_path)
        
        if len(signature_boxes) > 0:
            return True
        else:
            return False

        
    results = {}
    for count,proc_img_path in enumerate(affidavit.processed_image_paths.values(),start=1):
        results[count]=is_signature_present(proc_img_path)
    
    if True not in results.values():
        return {"issue":"Signature not found in affidavit",
                    "Rule": "Order IX Rule 7- Supreme court rules 2013"}
    else:
        return {}


def check_facts_from_knowledge_or_certification(affidavit):
    """
    Ensure that the affidavit is confined to facts that the deponent can prove from their own knowledge, or, if interpreted by a competent person elsewhere, that the affidavit is certified as correctly interpreted to the deponent.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the facts in the affidavit meet the knowledge or certification requirement.
    """
    pass
