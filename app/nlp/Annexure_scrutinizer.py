import importlib
import inspect
from .Document_scrutinizer import Document

class Annexure(Document):
    def annexure_trigger(self):
        self.certification()
        self.indexing_pagination()
        self.no_of_copies()

    def certification(self):
        module = importlib.import_module("..nlp.annexures.certification")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_certification= {}

        for func in functions:
                result = func(self)
                self.results_certification[func.__name__] = result

    
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
