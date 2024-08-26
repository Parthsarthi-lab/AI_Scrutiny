def check_cause_title(petition):
    """
    Check if the petition includes the correct Cause Title.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of the Cause Title.
    """
    pass

def check_extra_ordinary_jurisdiction(petition):
    """
    Check if the petition invokes the extra-ordinary jurisdiction under the correct article, typically Article 136.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the correct jurisdiction is invoked.
    """
    pass

def check_form_28(petition):
    """
    Check if the petition is filed in Form 28 as required.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the petition is filed in Form 28.
    """
    pass

def check_accompanied_documents(petition):
    """
    Check if the petition is accompanied by all required documents, including the list of dates, certified copies, and affidavits.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of all necessary documents.
    """
    pass

def check_list_of_dates(petition):
    """
    Check if the petition includes a list of dates in chronological order with relevant material facts or events.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence and correctness of the list of dates.
    """
    pass

def check_pleadings(petition):
    """
    Check if the petition is confined only to the pleadings before the Court/Tribunal whose order is challenged.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the petition is confined to the correct pleadings.
    """
    pass

def check_annexures(petition):
    """
    Check if the petition includes necessary annexures, which are certified copies of documents forming part of the record of the case.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of the necessary annexures.
    """
    pass

def check_additional_documents_application(petition):
    """
    Check if any additional documents not part of the record are included and whether a separate application seeking leave of the Court for their inclusion is made.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether additional documents and the necessary application are included.
    """
    pass

def check_english_version_provisions(petition):
    """
    Check if the English version of the relevant provisions of the Constitution, statutes, rules, etc., referred to in the impugned judgment, is filed as an appendix.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of the English version of relevant provisions.
    """
    pass

def check_affidavit_support(petition):
    """
    Check if the petition is supported by an affidavit, stating that the facts and dates furnished are true.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of the supporting affidavit.
    """
    pass

def check_previous_petitions(petition):
    """
    Check if the petition contains a statement about whether any previous petition for special leave to appeal was filed and the outcome.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the statement about previous petitions is included.
    """
    pass

def check_contesting_parties_info(petition):
    """
    Check if the petition contains the full name and address of all contesting parties if the matter was contested in the lower court.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of contesting parties' information.
    """
    pass

def check_lpa_or_wa(petition):
    """
    Check if the petition contains a statement about whether a Letters Patent Appeal or Writ Appeal lies against the impugned judgment and whether that remedy has been availed.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of the statement regarding Letters Patent Appeal or Writ Appeal.
    """
    pass

def check_certified_copies(petition):
    """
    Check if all annexures are certified copies, unless they are affirmed as true copies upon affidavit.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of certified copies or true copies affirmed by affidavit.
    """
    pass

def check_legal_representatives(petition):
    """
    Check if the petition includes a prayer and affidavit for bringing on record any person as the legal representative of a party.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of a prayer and affidavit for legal representatives.
    """
    pass

def check_defective_record_handling(petition):
    """
    Check if there is an application for substituting or entering on record the correct party if the record becomes defective.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether proper handling of a defective record is addressed.
    """
    pass

def check_subject_matter_value(petition):
    """
    Check if the petition states the amount or value of the subject-matter as required.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the subject-matter value is correctly stated.
    """
    pass

def check_contact_information(petition):
    """
    Check if the petition includes the name, description, registered address, fax number, and email address (if any) of each party.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of contact information for all parties.
    """
    pass

def check_status_of_parties(petition):
    """
    Check the status of parties (e.g., plaintiff, defendant, petitioner) in the Court below.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the correct status of parties in the Court below.
    """
    pass

def check_status_of_parties_in_appeal(petition):
    """
    Check the status of parties in the appeal, petition, or suit in case of a review or curative petition.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the correct status of parties in the appeal.
    """
    pass

def check_certified_judgment_copy(petition):
    """
    Check if a certified copy of the judgment or order appealed from is included.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of a certified copy of the judgment or order.
    """
    pass

def check_affidavit_in_support_of_facts(petition):
    """
    Check if the petition includes an affidavit supporting the statement of facts.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of an affidavit in support of the facts.
    """
    pass

def check_annexures_order(petition):
    """
    Check if the annexures are arranged in chronological order and properly indexed.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the annexures are in chronological order and indexed.
    """
    pass

def check_true_copies_affidavit(petition):
    """
    Check if uncertified copies of documents are affirmed to be true copies upon affidavit.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of affidavits affirming true copies of documents.
    """
    pass

def check_order_xxi_compliance(petition):
    """
    Check if the petition complies with Order XXI of the Rules of the Supreme Court.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating compliance with Order XXI.
    """
    pass
