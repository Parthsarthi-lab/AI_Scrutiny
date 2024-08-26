def check_heading_and_filing(affidavit):
    """
    Ensure that the affidavit is headed "In the Supreme Court of India" and filed in the cause, appeal, or matter for which it is sworn.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the heading and filing requirements are met.
    """
    pass

def check_structure_content(affidavit):
    """
    Verify that the affidavit is written in the first person, divided into consecutively numbered paragraphs, and includes the deponent’s description, occupation (if any), and true place of abode.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the structure and content of the affidavit meet the requirements.
    """
    pass

def check_pardahnashin_ladies(affidavit):
    """
    For deponents who are pardahnashin ladies, ensure the affidavit is affirmed or sworn before a lady Registrar or Oath Commissioner, and the deponent is identified by someone who knows her, with the identification proved by a separate affidavit.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the requirements for pardahnashin ladies are met.
    """
    pass

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
    pass

def check_facts_from_knowledge_or_certification(affidavit):
    """
    Ensure that the affidavit is confined to facts that the deponent can prove from their own knowledge, or, if interpreted by a competent person elsewhere, that the affidavit is certified as correctly interpreted to the deponent.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the facts in the affidavit meet the knowledge or certification requirement.
    """
    pass
