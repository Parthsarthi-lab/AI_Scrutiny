import re
def check_time_limit_for_filing(affidavit):
    """
    Confirm that the affidavit was filed within the time limits specified by the court. 
    If it is filed after the specified time, verify that it is accompanied by the court's permission for late filing.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the affidavit was filed within the time limit or has court permission for late filing.
    """
    pass

def check_time(affidavit):
    """
    Ensure that a diary number is generated and the date of filing is stamped on the affidavit. 
    Verify that the filing memo is complete with all necessary endorsements.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the filing memo is complete and the diary number and filing date are properly recorded.
    """
    text = ""
    for new in affidavit.text.values():
        text += new

    # Regular expression pattern
    pattern = r"Hence verified today the \d{1,2} day of (January|February|March|April|May|June|July|August|September|October|November|December) at \d{1,2}:\d{2} (am|pm)"

    # Check if the pattern is present in the string
    if re.search(pattern, text):
        return {}
    else:
        return {"issue":"Date and time is not mentioned in the affidavit",
                "Rule":"Order IX - Supreme Court Rules 2013"}

def check_affixing_court_fees(affidavit):
    """
    Verify that the appropriate court fees have been paid and affixed to the affidavit. 
    Ensure that the fees are punched or locked by the court to indicate they are used.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the court fees are properly affixed and marked as used.
    """
    pass

def check_unsigned_or_improperly_bound_documents(affidavit):
    """
    Check that the affidavit is properly signed and bound. 
    Ensure that unsigned documents or those with improper binding are not accepted.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the affidavit is properly signed and bound.
    """
    pass
