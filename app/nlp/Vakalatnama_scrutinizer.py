import importlib
import inspect
from .Document_scrutinizer import Document

class Vakalatnama(Document):
    def vakalatnama_trigger(self):
        self.execution()
        self.memo_appearance()

    def execution(self):
        module = importlib.import_module("..nlp.vakalatnama.execution")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_execution = {}

        for func in functions:
                result = func(self)
                self.results_execution[func.__name__] = result


    def memo_appearance(self):
        module = importlib.import_module("..nlp.vakalatnama.memo_appearance")

        functions = [func for name, func in inspect.getmembers(module, inspect.isfunction)]

        self.results_memo_appearance = {}

        for func in functions:
                result = func(self)
                self.results_memo_appearance[func.__name__] = result