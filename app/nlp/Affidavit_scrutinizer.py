import importlib
import inspect
from .Document_scrutinizer import Document

class Affidavit(Document):
    def affidavit_trigger(self):
        self.execution_verification()
        self.filing_requirements()
        self.filing_requirements()
        self.lang_translation()

    def execution_verification(self):
        module = importlib.import_module("..nlp.affidavits.execution_verification")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_execution = {}

        for func in functions:
                result = func(self)
                self.results_execution[func.__name__] = result

    def filing_requirements(self):
        module = importlib.import_module("..nlp.affidavits.filing_requirements")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_filing_requirements = {}

        for func in functions:
                result = func(self)
                self.results_filing_requirements[func.__name__] = result

    def lang_translation(self):
        module = importlib.import_module("..nlp.affidavits.lang_translation")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_lang_translation = {}

        for func in functions:
                result = func(self)
                self.results_lang_translation[func.__name__] = result

    def supporting_docs(self):
        module = importlib.import_module("..nlp.affidavits.supporting_docs")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_supporting_docs = {}

        for func in functions:
                result = func(self)
                self.results_supporting_docs[func.__name__] = result