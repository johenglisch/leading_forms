#! /usr/bin/env/python3

from leading_forms import *


leading_forms = [
    LeadingForm('r_1', {'masc': True,  'fem': False, 'gov': False, 'obl': False}),
    LeadingForm('n_2', {'masc': True,  'fem': False, 'gov': True,  'obl': False}),
    LeadingForm('m_3', {'masc': True,  'fem': False, 'gov': True,  'obl': True}),
    LeadingForm('s_4', {'masc': True,  'fem': False, 'gov': False, 'obl': True}),
    LeadingForm('s_5', {'masc': True,  'fem': True,  'gov': True,  'obl': False}),
    LeadingForm('e_6', {'masc': False, 'fem': True,  'gov': False, 'obl': False}),
    LeadingForm('n_7', {'masc': False, 'fem': False, 'gov': True,  'obl': True}),
    LeadingForm('r_8', {'masc': False, 'fem': True,  'gov': False, 'obl': True}),
    LeadingForm('r_9', {'masc': False, 'fem': False, 'gov': False, 'obl': True})]

constraints = [match, ident('masc'), ident('obl'), ident('fem'), ident('gov')]

paradigm = Paradigm(['obl', 'gov'], ['masc', 'fem'], leading_forms, constraints)
print(paradigm)
