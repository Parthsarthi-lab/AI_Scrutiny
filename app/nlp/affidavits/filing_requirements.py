def check_time_limit_for_filing(affidavit):
    """
    Confirm that the affidavit was filed within the time limits specified by the court. 
    If it is filed after the specified time, verify that it is accompanied by the court's permission for late filing.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the affidavit was filed within the time limit or has court permission for late filing.
    """
    pass

def check_filing_memo_and_diary_number(affidavit):
    """
    Ensure that a diary number is generated and the date of filing is stamped on the affidavit. 
    Verify that the filing memo is complete with all necessary endorsements.

    :param affidavit: The affidavit object containing all the necessary information and documents.
    :return: Tuple (boolean, message) indicating whether the filing memo is complete and the diary number and filing date are properly recorded.
    """
    pass

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
