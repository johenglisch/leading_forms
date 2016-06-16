#! /usr/bin/env/python3

from leading_forms import *


leading_forms = [
    LeadingForm('lo',   {'refl': False, '1': False, '2': False, 'pl': False, 'fem': False, 'gov': True,  'obl': False}),
    LeadingForm('la',   {'refl': False, '1': False, '2': False, 'pl': False, 'fem': True,  'gov': True,  'obl': False}),
    LeadingForm('li',   {'refl': False, '1': False, '2': False, 'pl': True,  'fem': False, 'gov': True,  'obl': False}),
    LeadingForm('le_1', {'refl': False, '1': False, '2': False, 'pl': True,  'fem': True,  'gov': True,  'obl': False}),
    LeadingForm('gli',  {'refl': False, '1': False, '2': False, 'pl': False, 'fem': False, 'gov': True,  'obl': True}),
    LeadingForm('le_2', {'refl': False, '1': False, '2': False, 'pl': False, 'fem': True,  'gov': True,  'obl': True}),
    LeadingForm('mi',   {'refl': False, '1': True,  '2': False, 'pl': False, 'fem': True,  'gov': True,  'obl': False}),
    LeadingForm('ti',   {'refl': False, '1': False, '2': True,  'pl': False, 'fem': True,  'gov': True,  'obl': False}),
    LeadingForm('ci',   {'refl': False, '1': True,  '2': False, 'pl': True,  'fem': True,  'gov': True,  'obl': False}),
    LeadingForm('vi',   {'refl': False, '1': False, '2': True,  'pl': True,  'fem': True,  'gov': True,  'obl': False}),
    LeadingForm('si',   {'refl': True,  '1': False, '2': False, 'pl': False, 'fem': True,  'gov': True,  'obl': False})]

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
