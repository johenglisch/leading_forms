#! /usr/bin/env/python3

from leading_forms import *


def no_gov_inanim(paradigm_cell, candidate):
    if all([not paradigm_cell['obl'],
            not paradigm_cell['subj'],
            not paradigm_cell['anim'],
            candidate.features['gov']]):
        return 1
    return 0


def match_gov_cl2_sg(paradigm_cell, candidate):
    if all([not paradigm_cell['a'],
            paradigm_cell['b'],
            paradigm_cell['gov'] != candidate.features['gov']]):
        return 1
    return 0


def main():
    leading_forms = [
        LeadingForm(1, 'a',      {'a': False, 'b': True,  'gov': False, 'subj': True,  'obl': False}),
        LeadingForm(2, 'u',      {'a': False, 'b': True,  'gov': True,  'subj': False, 'obl': False}),
        LeadingForm(3, 'y',      {'a': False, 'b': True,  'gov': True,  'subj': True,  'obl': False}),
        LeadingForm(4, '\u2205', {'a': True,  'b': False, 'gov': False, 'subj': True,  'obl': False}),
        LeadingForm(5, 'a',      {'a': True,  'b': False, 'gov': True,  'subj': True,  'obl': False})]

    constraints = [
        match_gov_cl2_sg,
        no_gov_inanim,
        match,
        ident('a'), ident('b'),
        ident('gov'), ident('obl'), ident('subj')]

    paradigm = Paradigm(
        ['obl', 'gov', 'subj'],
        ['anim', 'a', 'b'],
        leading_forms,
        constraints)

    paradigm.rows = [
        {'obl': False, 'gov': False, 'subj': True},
        {'obl': False, 'gov': True,  'subj': False},
        {'obl': False, 'gov': True,  'subj': True}]

    paradigm.columns = [
        {'anim': False, 'a': True,  'b': False},
        {'anim': False, 'a': False, 'b': True},
        {'anim': True,  'a': True,  'b': False},
        {'anim': True,  'a': False, 'b': True}]

    print(paradigm)

    print(tableau(
        constraints, paradigm.candidates,
        {'obl': False, 'gov': True, 'subj': False, 'a': True, 'b': False, 'anim': False},
        10))

    print(tableau(
        constraints, paradigm.candidates,
        {'obl': False, 'gov': True, 'subj': False, 'a': False, 'b': True, 'anim': False},
        10))



if __name__ == '__main__':
    main()
