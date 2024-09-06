import cv2
def check_legibility_and_format(documents):
    """
    Check that the contents of the application and annexures are clear, sharp, legible, in proper font size, and are double-spaced on one side of the paper.

    :param documents: A list or collection of documents, including the application and annexures.
    :return: Tuple (boolean, message) indicating whether the documents are legible and meet the format requirements.
    """
    pass

def check_certification_of_copies(documents):
    """
    Ensure that all annexures or documents filed along with the application are certified to be true copies by the advocate-on-record or the party in person.

    :param documents: A list or collection of documents, including the application and annexures.
    :return: Tuple (boolean, message) indicating whether the documents are certified to be true copies.
    """
    def detect_signature(image):
        """
        Detect possible signature regions in an image.

        Parameters:
        image (numpy.ndarray): The image to be processed.

        Returns:
        bool: True if a signature is detected, otherwise False.
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            
            # Filter based on typical signature dimensions (adjust these values as needed)
            if w > 50 and h > 20 and w > h:
                return True
        
        return False

    def check_annexure_for_signature():
        """
        Check if the last page of an annexure contains a signature.

        Parameters:
        pdf_path (str): The path to the annexure PDF file.

        Returns:
        bool: True if a signature is found, otherwise False.
        str: A message explaining the result.
        """
        # Extract the last page as an image

        last_page_image = cv2.imread(list(documents.processed_image_paths.values())[-1])
        
        # Detect signature on the last page
        signature_present = detect_signature(last_page_image)
        
        if signature_present:
            return {}
        else:
            return {"issue":"Copy is not certified to be true copy",
                    "rules":"Order XXI - Rule 5 - Supreme Court Rules 2013"}
        
    check_annexure_for_signature()

"""def check_endorsement_for_non_certified_copies(documents):
    ""
    If any document is not a certified copy, verify that it bears an endorsement stating that "it is not a certified copy".

    :param documents: A list or collection of documents, including any non-certified copies.
    :return: Tuple (boolean, message) indicating whether non-certified copies are properly endorsed.
    ""
    pass"""

"""def check_chronological_order(documents):
    ""
    Verify that the annexures are arranged in chronological order as marked in the index and within the body of the application.

    :param documents: A list or collection of annexures filed with the application.
    :return: Tuple (boolean, message) indicating whether the annexures are arranged in the correct chronological order.
    ""
    pass"""

"""def check_sealing_and_confidentiality(documents):
    ""
    For documents considered confidential or kept under sealed cover by the Court, ensure that no copies or extracts are provided unless ordered by the Chief Justice or the Court.

    :param documents: A list or collection of documents, including any that may be confidential.
    :return: Tuple (boolean, message) indicating whether the sealing and confidentiality requirements are met.
    ""
    pass

def check_certification_of_copies_for_use_in_court(documents):
    ""
    Ensure that every document filed for the use of the court is neatly and legibly presented, with clear endorsements that it is a true copy.

    :param documents: A list or collection of documents filed for the use of the court.
    :return: Tuple (boolean, message) indicating whether the documents are properly certified and presented for use in court.
    ""
    pass"""
