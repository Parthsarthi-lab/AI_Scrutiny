import re
import cv2
import numpy as np
import pytesseract
from PIL import Image

def check_signatures_on_vakalatnama(vakalatnama) :
    """
    Ensure that every vakalatnama in any cause, appeal, or matter is executed by the party.
    Verify that the names of the person(s) executing the vakalatnama and the advocate accepting it are mentioned below their respective signatures.

    :param vakalatnama: The vakalatnama document containing all the necessary information and signatures.
    :return: Tuple (boolean, message) indicating whether the signatures on the vakalatnama are correctly executed and identified.
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
    for count,proc_img_path in enumerate(vakalatnama.processed_image_paths.values(),start=1):
        results[count]=is_signature_present(proc_img_path)
    
    if True not in results.values():
        return {"issue":"Signature not found in affidavit",
                    "Rule": "Order IX Rule 7- Supreme court rules 2013"}
    else:
        return {}
    
def check_advocates_welfare_fund_stamp(vakalatnama):
    """
    Verify that the Advocates Welfare Fund Stamp is pasted on the header of the vakalatnama without covering any part of the text.
    Ensure that the stamp is properly cancelled; if not, the Vakalatnama is considered defective.

    :param vakalatnama: The vakalatnama document containing the Advocates Welfare Fund Stamp.
    :return: Tuple (boolean, message) indicating whether the stamp is correctly affixed and cancelled.
    """
    def detect_stamp_and_text(image):
        # Apply OCR to detect text regions
        h, w = image.shape
        d = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        
        text_boxes = []
        for i in range(len(d['level'])):
            (x, y, width, height) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            text_boxes.append((x, y, x + width, y + height))
        
        # Simple detection of a stamp-like region in the header area
        header_height = h // 5  # Assume header is the top 20% of the document
        stamp_region = image[:header_height, :]
        
        _, stamp_thresh = cv2.threshold(stamp_region, 150, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(stamp_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        stamp_box = None
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w > 50 and h > 50:  # Assuming the stamp has a significant size
                stamp_box = (x, y, x + w, y + h)
                break
        
        return stamp_box, text_boxes

    def validate_stamp_position(image_path):
        """
        Validate that the Advocates Welfare Fund Stamp is pasted on the header without covering any text.
        
        Parameters:
        image_path (str): The path to the preprocessed vakalatnama image.

        Returns:
        bool: True if the stamp is correctly placed, False otherwise.
        str: A message explaining the validation result.
        """
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        stamp_box, text_boxes = detect_stamp_and_text(image)
        
        if not stamp_box:
            return {"issue": "No stamp detected in the header area.",
                   "rules":"Rule d , Part III ,Chapter VIII of Handbook on Practice and Procedure and Office Procedure"}
        
        for box in text_boxes:
            if (box[0] < stamp_box[2] and box[2] > stamp_box[0]) and (box[1] < stamp_box[3] and box[3] > stamp_box[1]):
                return {"issue": "Stamp covering text",
                   "rules":"Rule d , Part III ,Chapter VIII of Handbook on Practice and Procedure and Office Procedure"}
        
        return {}

    # Example usage:
    is_valid = validate_stamp_position(vakalatnama.processed_image_paths[1])
    return is_valid

def check_format_and_compliance(vakalatnama):
    """
    Ensure that the vakalatnama is printed on A4 size paper and complies with all the required format specifications.

    :param vakalatnama: The vakalatnama document to be checked for format compliance.
    :return: Tuple (boolean, message) indicating whether the format of the vakalatnama complies with the specified requirements.
    """
    text = ""
    for new in vakalatnama.text.values():
        text += new

    # Convert text to lowercase for case-insensitive matching
    text = text.lower()

    # Define checks
    checks = {
        "heading": "vakalatnama" in text,
        "jurisdiction": re.search(r"in the supreme court of india\s*(criminal|civil|appellate|original)\s*jurisdiction", text) is not None,
        "case_details": re.search(r"crl\./civil/special leave petition/appeal/w\.p\. no\.", text) is not None,
        "roles": re.search(r"(appellant|petitioner|respondent)", text) is not None,
        "authorization_text": re.search(r"do hereby .* appoint .* retain .* advocate", text) is not None,
        "date_placeholder": re.search(r"date this the .* day of .*200", text) is not None,
    }

    if False in checks.values():
        return {"issue":"Vakalatnama not filed in proper format",
                "rule":"Chapter VIII of Handbook on Practice and Procedure and Office Procedure"}
    else:
        return {}

def check_identification_of_parties(vakalatnama):
    """
    Verify that the vakalatnama mentions the name, age, father’s name, and address of the person(s) appointing the advocate, 
    as well as the serial number in the array of parties.

    :param vakalatnama: The vakalatnama document containing the details of the parties.
    :return: Tuple (boolean, message) indicating whether the identification of parties is correctly mentioned.
    """
    pass

def check_certification_and_witnessing(vakalatnama):
    """
    Ensure that where the advocate on-record merely accepts the vakalatnama, which is already duly executed in the presence of a Notary or an advocate,
    he makes an endorsement that he has satisfied himself about the due execution of the vakalatnama.
    Where the vakalatnama is executed in the presence of the advocate on-record, he shall certify that it was executed in his presence.

    :param vakalatnama: The vakalatnama document to be checked for proper certification and witnessing.
    :return: Tuple (boolean, message) indicating whether the vakalatnama has been properly certified and witnessed.
    """
    pass

def check_details_of_parties(vakalatnama):
    """
    Ensure that the vakalatnama contains the State Bar Council Enrolment Number, postal address, telephone number, mobile number,
    email address, and registration number of the advocate on-record accepting the vakalatnama, for service.
    Verify that it also includes the name of the person(s) executing the vakalatnama and the advocate accepting the same, below their respective signatures.

    :param vakalatnama: The vakalatnama document containing the details of the parties.
    :return: Tuple (boolean, message) indicating whether the details of the parties are correctly mentioned and complete.
    """
    pass

def check_power_of_attorney_attachments(vakalatnama):
    """
    Ensure that if a person other than a party to the cause, appeal, or matter files the vakalatnama on the basis of Power of Attorney,
    the original Power of Attorney is annexed with the vakalatnama.

    :param vakalatnama: The vakalatnama document to be checked for the proper annexing of Power of Attorney.
    :return: Tuple (boolean, message) indicating whether the Power of Attorney is correctly attached.
    """
    pass
