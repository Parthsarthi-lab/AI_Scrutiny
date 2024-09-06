import importlib
import inspect
from .Document_scrutinizer import Document
from ..nlp.slp.slp_civil import *


class SLP(Document):

    def __init__(self,file,lod=None,translated_file_path=None,list_of_dates_path=None):
        self.translated_file_path = translated_file_path
        self.list_of_dates_path = list_of_dates_path
        self.list_of_dates = lod
        super().__init__(file)

    def slp_trigger(self):

        #Write logic to check the type of slp
        # Convert text to lowercase for uniformity
        text=""
        for i in self.text.values():
            text = text+" "+i
            
        text = text.lower()
        # Define keywords for civil and criminal cases
        civil_keywords = ["contract", "property", "family law", "torts", "divorce", "inheritance", "company law", "arbitration", "cpc", "specific relief act"]
        criminal_keywords = ["murder", "theft", "criminal", "penal", "imprisonment", "sentence", "bail", "fir", "chargesheet", "ipc", "accused", "prosecution", "crpc", "evidence act"]

        # Initialize counts for civil and criminal indicators
        civil_count = 0
        criminal_count = 0

        # Count occurrences of civil keywords
        for keyword in civil_keywords:
            civil_count += text.count(keyword)

        # Count occurrences of criminal keywords
        for keyword in criminal_keywords:
            criminal_count += text.count(keyword)

        # Determine the type based on counts
        if civil_count > criminal_count:
            #print("Civil SLP") # remove this line later on
            self.slp_civil()

        elif criminal_count > civil_count:
            #print("Criminal SLP") # remove this line later on
            self.slp_criminal()
        else:
            self.slp_defects = {}
            self.slp_defects.update(self.common_defects)
        
        """if self.case=="Civil":
            self.slp_civil()
        elif self.case=="Criminal":
            self.slp_criminal()"""

    def slp_civil(self):
        self.slp_defects = {}
        self.slp_defects.update(self.common_defects)
        self.slp_defects["format_check_errors"] = check_form_28(self) # this is a dictionary
        self.slp_defects["list_of_dates_errors"] = check_list_of_dates(self,self.list_of_dates)
        
        
        #check_cause_title(self)
        #check_extra_ordinary_jurisdiction(self)
        #check_accompanied_documents(self)
        """check_pleadings(self)
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
        #check_order_xxi_compliance(self)"""

    def slp_criminal(self):
        self.slp_defects = {}
        self.slp_defects.update(self.common_defects)
        self.slp_defects["format_check_errors"] = check_form_28(self) 
        self.slp_defects["list_of_dates_errors"] = check_list_of_dates(self,self.list_of_dates)
        