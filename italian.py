#! /usr/bin/env/python3

from leading_forms import *


leading_forms = [
    LeadingForm( 1, 'lo',  {'refl': False, '1': False, '2': False, 'pl': False, 'fem': False, 'gov': True,  'obl': False}),
    LeadingForm( 2, 'la',  {'refl': False, '1': False, '2': False, 'pl': False, 'fem': True,  'gov': True,  'obl': False}),
    LeadingForm( 3, 'li',  {'refl': False, '1': False, '2': False, 'pl': True,  'fem': False, 'gov': True,  'obl': False}),
    LeadingForm( 4, 'le',  {'refl': False, '1': False, '2': False, 'pl': True,  'fem': True,  'gov': True,  'obl': False}),
    LeadingForm( 5, 'gli', {'refl': False, '1': False, '2': False, 'pl': False, 'fem': False, 'gov': True,  'obl': True}),
    LeadingForm( 6, 'le',  {'refl': False, '1': False, '2': False, 'pl': False, 'fem': True,  'gov': True,  'obl': True}),
    LeadingForm( 7, 'mi',  {'refl': False, '1': True,  '2': False, 'pl': False, 'fem': True,  'gov': True,  'obl': False}),
    LeadingForm( 8, 'ti',  {'refl': False, '1': False, '2': True,  'pl': False, 'fem': True,  'gov': True,  'obl': False}),
    LeadingForm( 9, 'ci',  {'refl': False, '1': True,  '2': False, 'pl': True,  'fem': True,  'gov': True,  'obl': False}),
    LeadingForm(10, 'vi',  {'refl': False, '1': False, '2': True,  'pl': True,  'fem': True,  'gov': True,  'obl': False}),
    LeadingForm(11, 'si',  {'refl': True,  '1': False, '2': False, 'pl': False, 'fem': True,  'gov': True,  'obl': False})]

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
