from .Document_scrutinizer import Document
from .vakalatnama.memo_appearance import *
class Memo_of_appearance(Document):
    def memo_trigger(self):
        self.memo_of_appearance_defects = {}
        self.memo_of_appearance_defects.update(self.common_defects)
        self.memo_of_appearance_defects["Execution & Verification"]=self.memo_appearance()
        

    def memo_appearance(self):
        declaration_by_AOR = check_declaration_by_advocate_on_record(self)
        
        if declaration_by_AOR == {}:
            declaration_by_AOR = None

        return [declaration_by_AOR]
