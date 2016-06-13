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


## Constraints ##

class Ident:
    def __init__(self, feature):
        self.feature = feature

    def __call__(self, cell, cand):
        if cand.leading_form.features[self.feature] == cand.features[self.feature]:
            return 0
        return 1


def match(paradigm_cell, candidate):
    return sum(
        paradigm_cell[f] != candidate.features[f]
        for f in candidate.features)


## Functions ##

def optimise(constraints, candidates, paradigm_cell):
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
