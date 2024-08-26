def check_document_language(affidavit):
    """
    Ensure that the affidavit and its supporting documents are written in English. 
    If any document is not in English, verify that it is accompanied by an accurate translation into English.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the language of the documents is English or if a correct translation is provided.
    """
    pass

def check_translation_approval(affidavit):
    """
    Confirm that any non-English document is accompanied by a translation that meets one of the following criteria:
    - A translation agreed upon by both parties.
    - A translation certified as true by a court-appointed translator.
    - A translation by a translator approved and notified by the Court.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the translation is properly approved according to the specified criteria.
    """
    pass

def check_correctness_of_translation(affidavit):
    """
    Verify that the translation is accurate, complete, and corresponds exactly with the original document. 
    Inaccurate or incomplete translations can result in the document being rejected or the case being delayed.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the translation is accurate and complete.
    """
    pass

def check_interpreters_certification(affidavit):
    """
    If the affidavit requires interpretation for the deponent (e.g., the deponent doesn't speak the language in which the affidavit is written), 
    ensure that it was interpreted by an approved interpreter. 
    The interpreter must certify that the affidavit was correctly interpreted to the deponent.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the interpreter's certification is present and valid.
    """
    pass
