#! /usr/bin/env/python3

from leading_forms import *


def main():
    leading_forms = [
        LeadingForm(1, 'r', {'m': True,  'f': False, 'g': False, 'o': False}),
        LeadingForm(2, 'n', {'m': True,  'f': False, 'g': True,  'o': False}),
        LeadingForm(3, 'm', {'m': True,  'f': False, 'g': True,  'o': True}),
        LeadingForm(4, 's', {'m': True,  'f': False, 'g': False, 'o': True}),
        LeadingForm(5, 's', {'m': True,  'f': True,  'g': True,  'o': False}),
        LeadingForm(6, 'e', {'m': False, 'f': True,  'g': False, 'o': False}),
        LeadingForm(7, 'n', {'m': False, 'f': False, 'g': True,  'o': True}),
        LeadingForm(8, 'r', {'m': False, 'f': True,  'g': False, 'o': True}),
        LeadingForm(9, 'r', {'m': False, 'f': False, 'g': False, 'o': True})]

    constraints = [match, ident('m'), ident('o'), ident('f'), ident('g')]

    paradigm = Paradigm(['o', 'g'], ['m', 'f'], leading_forms, constraints)
    print(paradigm)


if __name__ == '__main__':
    main()
