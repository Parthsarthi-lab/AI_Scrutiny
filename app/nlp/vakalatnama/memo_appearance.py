def check_declaration_by_advocate_on_record(vakalatnama):
    """
    Ensure that the vakalatnama consists of a declaration signed by the advocate on-record, stating that he has been authorized, instructed, and engaged to appear, act, and plead for the party.

    :param vakalatnama: The vakalatnama document containing the declaration by the advocate on-record.
    :return: Tuple (boolean, message) indicating whether the declaration by the advocate on-record is present and correctly signed.
    """
    pass

def check_counter_signature_by_party(vakalatnama):
    """
    If the party has personally authorized the Advocate-on-Record, verify that the memo of appearance is counter-signed by the party.

    :param vakalatnama: The vakalatnama document containing the memo of appearance.
    :return: Tuple (boolean, message) indicating whether the memo of appearance is counter-signed by the party.
    """
    pass

def check_power_of_attorney(vakalatnama):
    """
    If someone other than the party has authorized the Advocate-on-Record on behalf of the party, check that the memo of appearance is accompanied by a Power of Attorney signed by the party. 
    This Power of Attorney should clearly state the relationship between the party and the person authorizing the representation.

    :param vakalatnama: The vakalatnama document containing the memo of appearance and Power of Attorney.
    :return: Tuple (boolean, message) indicating whether the Power of Attorney is present and correctly executed.
    """
    pass

def check_thumb_impression_or_mark(affidavit, party):
    """
    For an illiterate party, confirm that their thumb impression or mark is attested by at least two literate witnesses. 
    Verify that the names and addresses of these witnesses are provided.

    :param affidavit: The affidavit document containing the thumb impression or mark of the party.
    :param party: The party details object containing information about the party.
    :return: Tuple (boolean, message) indicating whether the thumb impression or mark is properly attested by two witnesses with their names and addresses provided.
    """
    pass

def check_power_of_attorney_provided(vakalatnama):
    """
    Verify that a Power of Attorney is provided if someone other than the party has authorized the Advocate-on-Record. 
    If the Power of Attorney is not provided, treat the case as defective.

    :param vakalatnama: The vakalatnama document to be checked for the presence of Power of Attorney.
    :return: Tuple (boolean, message) indicating whether the Power of Attorney is provided. 
             If not provided, the function should return a message indicating that the case is defective.
    """
    pass
