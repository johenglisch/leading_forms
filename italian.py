#! /usr/bin/env/python3

from leading_forms import *


leading_forms = [
    LeadingForm('lo',   parse_features('-refl -1 -2 -pl -fem +gov -obl')),
    LeadingForm('la',   parse_features('-refl -1 -2 -pl +fem +gov -obl')),
    LeadingForm('li',   parse_features('-refl -1 -2 +pl -fem +gov -obl')),
    LeadingForm('le_1', parse_features('-refl -1 -2 +pl +fem +gov -obl')),
    LeadingForm('gli',  parse_features('-refl -1 -2 -pl -fem +gov +obl')),
    LeadingForm('le_2', parse_features('-refl -1 -2 -pl +fem +gov +obl')),
    LeadingForm('mi',   parse_features('-refl +1 -2 -pl +fem +gov -obl')),
    LeadingForm('ti',   parse_features('-refl -1 +2 -pl +fem +gov -obl')),
    LeadingForm('ci',   parse_features('-refl +1 -2 +pl +fem +gov -obl')),
    LeadingForm('vi',   parse_features('-refl -1 +2 +pl +fem +gov -obl')),
    LeadingForm('si',   parse_features('+refl -1 -2 -pl +fem +gov -obl'))]

constraints = [
    match,
    ident('1'), ident('2'),
    ident('refl'),
    ident('pl'),
    ident('fem'),
    ident('gov'), ident('obl')]

paradigm = Paradigm(
    ['refl', 'obl'],
    ['pl', '1', '2', 'fem'],
    leading_forms,
    constraints,
    default_features = {'gov': True})

print(paradigm)
