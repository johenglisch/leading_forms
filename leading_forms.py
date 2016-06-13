from itertools import product
from functools import partial
from collections import ChainMap


## Helper functions ##

def features_to_str(features):
    return ' '.join(
        '{val}{feat}'.format(feat=f, val='+' if features[f] else '-')
        for f in sorted(features))


## Structs ##

class LeadingForm:
    def __init__(self, index, phon, features):
        self.index = index
        self.phon = phon
        self.features = features

    def __str__(self):
        return '{phon}_{index} \u2194 [{features}]'.format(
            phon=self.phon,
            index=self.index,
            features=features_to_str(self.features))


class Candidate:
    def __init__(self, leading_form, features):
        self.leading_form = leading_form
        self.features = features

    def __str__(self):
        return '<{phon}_{index}, [{features}]>'.format(
            phon=self.leading_form.phon,
            index=self.leading_form.index,
            features=features_to_str(self.features))


class Paradigm:
    def __init__(
            self, row_features, column_features, leading_forms, constraints,
            candidates=None):
        self.rows = list(permutate_features(row_features))
        self.columns = list(permutate_features(column_features))
        self.features = row_features + column_features
        self.leading_forms = leading_forms
        self.constraints = constraints
        self.candidates = (
            candidates if candidates is not None
            else list(permutate_forms(leading_forms, self.features)))
        self.filled = None

    def realise_cells(self):
        self.filled = [
            [realise(self.constraints, self.candidates, ChainMap(r, c))
             for c in self.columns]
            for r in self.rows]

    def __str__(self):
        if self.filled is None:
            self.realise_cells()
        strings = [
            [list(map(str, cell)) for cell in row]
            for row in self.filled]
        heights = [max(map(len, row)) for row in strings]
        widths = [max(
                max(map(len, strings[row][col]))
                for row in range(len(strings)))
            for col in range(len(strings[0]))]


## Constraints ##

def match(paradigm_cell, candidate):
    return sum(
        paradigm_cell[f] != candidate.features[f]
        for f in candidate.features)


def _general_ident(feature, paradigm_cell, candidate):
    if candidate.leading_form.features[feature] == candidate.features[feature]:
        return 0
    return 1


def ident(feature):
    return partial(_general_ident, feature)


## Functions ##

def permutate_features(features):
    return (
        dict(zip(features, permutation))
        for permutation in product((True, False), repeat=len(features)))

def permutate_forms(leading_forms, features):
    possible_specs = list(permutate_features(features))
    return (
        Candidate(form, spec)
        for form in leading_forms
        for spec in possible_specs)


def realise(constraints, candidates, paradigm_cell):
    optimal = None
    outputs = list()
    for candidate in candidates:
        violations = tuple(c(paradigm_cell, candidate) for c in constraints)
        if optimal is None or optimal > violations:
            optimal = violations
            outputs = list()
        if optimal == violations:
            outputs.append(candidate)
    return outputs
