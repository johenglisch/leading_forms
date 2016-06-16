#! /usr/bin/env/python3

"""Analysis of German determiner inflection without underspecification."""

from leading_forms import *


leading_forms = [
    LeadingForm('r_1', parse_features('+masc -fem -gov -obl')),
    LeadingForm('n_2', parse_features('+masc -fem +gov -obl')),
    LeadingForm('m_3', parse_features('+masc -fem +gov +obl')),
    LeadingForm('s_4', parse_features('+masc -fem -gov +obl')),
    LeadingForm('s_5', parse_features('+masc +fem +gov -obl')),
    LeadingForm('e_6', parse_features('-masc +fem -gov -obl')),
    LeadingForm('n_7', parse_features('-masc -fem +gov +obl')),
    LeadingForm('r_8', parse_features('-masc +fem -gov +obl')),
    LeadingForm('r_9', parse_features('-masc -fem -gov +obl'))]

constraints = [match, ident('masc'), ident('obl'), ident('fem'), ident('gov')]

paradigm = Paradigm(['obl', 'gov'], ['masc', 'fem'], leading_forms, constraints)
print(paradigm)
