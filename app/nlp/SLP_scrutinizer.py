import importlib
import inspect
from .Document_scrutinizer import Document
from ..nlp.slp.slp_civil import *


class SLP(Document):
    def slp_trigger(self):

        #Write logic to check the type of slp
        pass
        
        if self.case=="Civil":
            self.slp_civil()
        elif self.case=="Criminal":
            self.slp_criminal()

    def slp_civil(self):
        check_cause_title(self)
        check_extra_ordinary_jurisdiction(self)
        check_form_28(self)
        check_accompanied_documents(self)
        check_list_of_dates(self)
        check_pleadings(self)
        check_annexures(self)
        check_additional_documents_application(self)
        check_english_version_provisions(self)
        check_affidavit_support(self)
        check_previous_petitions(self)
        check_contesting_parties_info(self)
        check_lpa_or_wa(self)
        check_certified_copies(self)
        check_legal_representatives(self)
        check_defective_record_handling(self)
        check_subject_matter_value(self)
        check_contact_information(self)
        check_status_of_parties(self)
        check_status_of_parties_in_appeal(self)
        check_certified_judgment_copy(self)
        check_affidavit_in_support_of_facts(self)
        check_annexures_order(self)
        check_true_copies_affidavit(self)
        check_order_xxi_compliance(self)

    def slp_criminal(self):
        module = importlib.import_module("..nlp.slp.slp_criminal")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results = {}

        for func in functions:
                result = func(self)
                self.results[func.__name__] = result

