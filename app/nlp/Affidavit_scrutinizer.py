import importlib
import inspect
from .Document_scrutinizer import Document
from ..nlp.affidavits.execution_verification import *
from ..nlp.affidavits.filing_requirements import *
class Affidavit(Document):
    def affidavit_trigger(self):
        self.affidavit_defects = {}
        self.affidavit_defects.update(self.common_defects)
        self.affidavit_defects["Execution & Verification"]=self.execution_verification()
        self.affidavit_defects["Filing Requirements"] = self.filing_requirements()
        
        #self.lang_translation()

    def execution_verification(self):
        heading = check_heading_and_filing(self)
        content = check_structure_content(self)
        signature_swearing = check_signing_and_swearing(self)

        if heading == {}:
            heading = None
        if signature_swearing == {}:
            signature_swearing = None
        if content =={}:
            content = None
        
        return [heading,content,signature_swearing]

    def filing_requirements(self):
        time_mention = check_time(self)

        if time_mention =={}:
            time_mention = None
        return [time_mention]

    """def supporting_docs(self):
        module = importlib.import_module("..nlp.affidavits.supporting_docs")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_supporting_docs = {}

        for func in functions:
                result = func(self)
                self.results_supporting_docs[func.__name__] = result"""