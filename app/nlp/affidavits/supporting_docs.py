def check_exhibits_and_annexures_marking(affidavit):
    """
    Ensure that every exhibit or annexure attached to the affidavit is clearly marked with the title and number of the cause, appeal, or matter. 
    Each exhibit should be initialed and dated by the authority before whom the affidavit is sworn.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the exhibits and annexures are properly marked, initialed, and dated.
    """
    pass

def check_certified_copies(annexures):
    """
    Check that annexures to the petition are certified copies of documents that formed part of the record in the court appealed from. 
    Uncertified copies may only be accepted if they are affirmed to be true copies by affidavit.

    :param annexures: The annexures attached to the petition.
    :return: Tuple (boolean, message) indicating whether the annexures are certified copies or properly affirmed as true copies.
    """
    pass

def check_language_of_documents(documents):
    """
    Verify that all supporting documents are in English. If any document is in another language, it must be accompanied by an agreed translation, 
    a certified translation by a court-appointed translator, or a translation approved by the court.

    :param documents: A list or collection of documents attached to the petition or affidavit.
    :return: Tuple (boolean, message) indicating whether the language requirements for documents are met.
    """
    pass
