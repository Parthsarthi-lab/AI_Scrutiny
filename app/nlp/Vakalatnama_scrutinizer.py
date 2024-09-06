import importlib
import inspect
from .Document_scrutinizer import Document
from .vakalatnama.execution import *
class Vakalatnama(Document):
    def vakalatnama_trigger(self):
        self.vakalatnama_defects = {}
        self.vakalatnama_defects.update(self.common_defects)
        self.vakalatnama_defects["Execution & Verification"]=self.execution()
        
        

    def execution(self):
        signature_error = check_signatures_on_vakalatnama(self)
        adv_welfare_fund_stamp_error = check_advocates_welfare_fund_stamp(self)
        format_error = check_format_and_compliance(self)

        if signature_error == {}:
            signature_error = None
        if adv_welfare_fund_stamp_error =={}:
            adv_welfare_fund_stamp_error = None
        if format_error == {}:
            format_error = None
            
        return [signature_error,adv_welfare_fund_stamp_error,format_error]


    