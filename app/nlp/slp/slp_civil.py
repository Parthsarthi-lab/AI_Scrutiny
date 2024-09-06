import spacy
import re
import fitz  # PyMuPDF
import os
from datetime import datetime

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def check_form_28(petition):
    """
    Check if the petition is filed in Form 28 as required.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the petition is filed in Form 28.
    """
     # Convert text to lowercase for uniformity
    text=""
    for i in petition.text.values():
        text = text+" "+i

    text = text.lower()
    print(text)
     # Define regex patterns for each key component of Form 28
    patterns = {
        "title": r"special leave petition.*under article 136 of the constitution of india",
        "case_information": r"s\.l\.p\. \(criminal\) no\..*\d{4}",
        "addressing_court": r"to\s+hon'ble the chief justice of india",
        "introduction": r"petitioner.*submits.*petition.*special leave to appeal",
        "questions_of_law": r"question[s]?\s+of\s+law",
        "declaration_rule_4_2": r"declaration.*terms of rule 4\(2\)",
        "declaration_rule_6": r"declaration.*terms of rule 6",
        "grounds_for_appeal": r"grounds",
        "grounds_for_interim_relief": r"grounds for interim relief",
        "main_prayer": r"main prayer",
        "interim_relief": r"interim relief",
        "signatures_verification": r"advocate for the petitioner.*\s+by the order of the court"
    }

    # Initialize a dictionary to store the check results
    format_check_results = {}

    # Check each pattern in the text
    for component, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            format_check_results[component] = "Found"
        else:
            format_check_results[component] = "Not Found or Incorrectly Formatted"

    # Determine if the document follows Form 28 based on the presence of all key components
    if all(value == "Found" for value in format_check_results.values()):
        format_check_results["form_28_compliance"] = "The document appears to be written in Form 28 format."
        return None
    else:
        issues_dict = {key: value for key, value in format_check_results.items() if value == "Not Found or Incorrectly Formatted"}
        return issues_dict

    


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

def check_accompanied_documents(petition):
    """
    Check if the petition is accompanied by all required documents, including the list of dates, certified copies, and affidavits.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence of all necessary documents.
    """
    pass

def check_list_of_dates(petition,lod):
    """
    Check if the petition includes a list of dates in chronological order with relevant material facts or events.

    :param petition: The petition object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating the presence and correctness of the list of dates.
    """
    
    lod_file_path = petition.list_of_dates_path
    
    if lod_file_path is None:
        return {
                "issue": "List of Dates not attached",
                "Rules": "Order XXI Rule 3(1)(b)- Supreme Court Rules 2013"
                }
    elif not os.path.exists(lod_file_path) :
        
        return {
                "issue": "List of Dates not attached",
                "Rules": "Order XXI Rule 3(1)(b)- Supreme Court Rules 2013"
                }
    else:
        date_formats = ["%d.%m.%Y","%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%Y/%m/%d", "%B %d, %Y", "%d %B %Y"]
    
        def is_valid_date(date_string):
            """Check if the given string is a valid date."""
            for date_format in date_formats:
                try:
                    datetime.strptime(date_string, date_format)
                    return True
                except ValueError:
                    continue
            return False

        
        text = ""
        for content in lod.text.values():
            text += content
        # Use regex to find potential date patterns
        date_pattern = r'\b(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2}|\w+ \d{1,2}, \d{4})\b'

        potential_dates = re.findall(date_pattern, content)

        valid_dates = [date for date in potential_dates if is_valid_date(date)]
        invalid_dates = [date for date in potential_dates if not is_valid_date(date)]

        if valid_dates and not invalid_dates:
            return None
        else:
            return {
            "issue": "Dates not found",
                "Rules": "Order XXI Rule 3(1)(b)- Supreme Court Rules 2013"
            }
    
    



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
