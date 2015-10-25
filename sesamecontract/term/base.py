from abc import ABCMeta, abstractmethod

class Term():
    __metaclass__ = ABCMeta

    def __init__(self, fragment, term_type):
        self.fragment = fragment
        self.term_type = term_type
        self.term = None

    def write_term(self):
        if not self.term:
            self.term = self.compute_term()
        return self.term

    @abstractmethod
    def compute_term(self):
        pass
