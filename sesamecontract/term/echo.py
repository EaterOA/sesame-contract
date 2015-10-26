from sesamecontract.term import Term

class EchoTerm(Term):

    def __init__(self, fragment):
        super().__init__(fragment, 'echo')

    def compute_term(self):
        return self.fragment
