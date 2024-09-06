import importlib
import inspect
from .Document_scrutinizer import Document
from .annexures.certification import *

class Annexure(Document):
    
    def __init__(self,file,translated_file_path=None):
        self.translated_file_path = translated_file_path
        super().__init__(file)

    def annexure_trigger(self):
        self.annexure_defects = {}
        self.annexure_defects.update(self.common_defects)
        self.annexure_defects["Certification"] = self.certification()
        #self.indexing_pagination()
        #self.no_of_copies()

    def certification(self):
        certification_of_copies = check_certification_of_copies(self)

        if certification_of_copies == {}:
             certification_of_copies = None

        return [certification_of_copies]

    def indexing_pagination(self):
        module = importlib.import_module("..nlp.annexures.indexing_pagination")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_indexing_pagination= {}

        for func in functions:
                result = func(self)
                self.results_indexing_pagination[func.__name__] = result

    def no_of_copies(self):
        module = importlib.import_module("..nlp.annexures.no_of_copies")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_copies= {}

        for func in functions:
                result = func(self)
                self.results_copies[func.__name__] = result
