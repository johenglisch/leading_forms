#! /usr/bin/env/python3

from leading_forms import *


leading_forms = [
    LeadingForm(1, 'r', {'masc': True,  'fem': False, 'gov': False, 'obl': False}),
    LeadingForm(2, 'n', {'masc': True,  'fem': False, 'gov': True,  'obl': False}),
    LeadingForm(3, 'm', {'masc': True,  'fem': False, 'gov': True,  'obl': True}),
    LeadingForm(4, 's', {'masc': True,  'fem': False, 'gov': False, 'obl': True}),
    LeadingForm(5, 's', {'masc': True,  'fem': True,  'gov': True,  'obl': False}),
    LeadingForm(6, 'e', {'masc': False, 'fem': True,  'gov': False, 'obl': False}),
    LeadingForm(7, 'n', {'masc': False, 'fem': False, 'gov': True,  'obl': True}),
    LeadingForm(8, 'r', {'masc': False, 'fem': True,  'gov': False, 'obl': True}),
    LeadingForm(9, 'r', {'masc': False, 'fem': False, 'gov': False, 'obl': True})]

constraints = [match, ident('masc'), ident('obl'), ident('fem'), ident('gov')]

paradigm = Paradigm(['obl', 'gov'], ['masc', 'fem'], leading_forms, constraints)
print(paradigm)
