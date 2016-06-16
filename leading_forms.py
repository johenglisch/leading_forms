"""leading_forms.

Implementation of Mueller's (2011)[1] framework of Syncretism without
Underpecification.

 [1] Mueller, Gereon (2011):  'Syncretism without underspecification:  The role
     of leading forms.'  Word Structure 4.1, 53-103.

"""

from itertools import chain, product, zip_longest
from functools import partial
from collections import ChainMap


## Helper functions ##

# Feature permutation

def permutate_features(features):
    """Lazily generate all combinations of values for a list of features."""
    return (
        dict(zip(features, permutation))
        for permutation in product((False, True), repeat=len(features)))

def permutate_forms(leading_forms, features):
    """Lazily generate output candidates.

    All leading forms are combined with all possible values for a list of
    features.

    """
    possible_specs = list(permutate_features(features))
    return (
        Candidate(form, spec)
        for form in leading_forms
        for spec in possible_specs)


# Pretty-printing features

def render_feature(feature_tuple):
    """Convert a (feature, value) tuple into a string."""
    feat, val = feature_tuple
    return '{val}{feat}'.format(feat=feat, val='+' if val else '-')

def render_featureset(features):
    """Convert a dictionary of binary features into a string."""
    return ' '.join(map(render_feature, sorted(features.items())))

def parse_features(string):
    """Convert a string like '+feat1 -feat2 +feat2' into a feature dict."""
    return dict(
        (elem[1:], elem[0] == '+') for elem in string.split())


# Pretty-printing tables

def max_lengths(rows):
    """Return a maximum length for each each column in rows as a list."""
    return [max(max(map(len, c)) for c in col) for col in zip(*rows)]

def render_line(line, lengths):
    """Convert a list of cells into a string.

    Each cell is padded to its corresponding length.

    """
    return '  '.join(
        '{cell:<{len}}'.format(
            cell=cell if cell is not None else '',
            len=length)
        for cell, length in zip(line, lengths))

def render_row(row, lengths):
    """Convert a list of line lists into a string."""
    lines = (
        ' {} '.format(render_line(line, lengths))
        for line in zip_longest(*row))
    return '\n'.join(lines)

def ascii_table(rows):
    """Convert a list of rows into an ascii table."""
    lengths = max_lengths(rows)
    dline = '=' * (sum(lengths) + 2 * len(lengths))
    sline = '-' * (sum(lengths) + 2 * len(lengths))

    lines = [dline, render_row(rows[0], lengths), sline]
    lines.extend(render_row(row, lengths) for row in rows[1:])
    lines.append(dline)

    return '\n'.join(lines)


## Structs ##

class LeadingForm:
    """Representation of a leading form.

    self.phon:     Phonogical representation.
    self.features: Dictionary of binary morpho-syntactic features.

    """

    def __init__(self, phon, features):
        """Create a leading form from a phonological representation and
        a dictionary of morpho-syntactic features.

        """
        self.phon = phon
        self.features = features

    def __str__(self):
        """Return string representation of a leading form."""
        return '{phon} \u2194 [{features}]'.format(
            phon=self.phon,
            features=render_featureset(self.features))


class Candidate:
    """Output candidate of the optimisation process.

    self.leading_form: Leading form inserted into a context.
    self.features:     Dictionary of binary morpho-syntactic features.

    """

    def __init__(self, leading_form, features):
        """Create a candidate from a leading form and a dictionary of
        morpho-syntactic features.

        """
        self.leading_form = leading_form
        self.features = features

    def phon(self):
        """Return phonological representation of a candidate."""
        return self.leading_form.phon

    def __str__(self):
        """Return string representation of a candidate."""
        return '<{phon}, [{features}]>'.format(
            phon=self.leading_form.phon,
            features=render_featureset(self.features))


class Paradigm:
    """Inflectional paradigm.

    self.features:         List of specified morpho-syntactic features.
    self.rows:             List of feature sets for each row.
    self.columns:          List of feature sets for each column.
    self.leading_forms:    Leading forms applicable to the paradigm.
    self.constraints:      Ordered list of constraints.
    self.default_features: Default values for features.

    """

    def __init__(
            self, row_features, column_features, leading_forms, constraints,
            default_features=None, candidates=None):
        """Create new paradgim.

        row_features:     Features for each row.
        column_features:  Features for each column.
        leading_forms:    Leading forms applicable to the paradigm.
        constraints:      Ordered list of constraints.
        default_features: Default values for features.
        candidates:       List of output candidates (tries every leading form
                          with every feature-value mapping by default).

        """
        self.rows = list(permutate_features(row_features))
        self.columns = list(permutate_features(column_features))
        self.leading_forms = leading_forms
        self.constraints = constraints
        self.default_features = (
            default_features if default_features is not None
            else dict())

        self.features = set(chain(
            self.default_features.keys(), row_features, column_features))

        self.candidates = (
            candidates if candidates is not None
            else list(permutate_forms(leading_forms, self.features)))

        self._filled = None

    def _realise_cells(self):
        self._filled = [
            [realise(
                self.constraints,
                self.candidates,
                ChainMap(r, c, self.default_features))
             for c in self.columns]
            for r in self.rows]

    def derivation(self, feature_string, max_lines=None):
        """Return OT tableau for a single paradgim cell as a string.

        The tableau includes the `max_lines` most optimal candidates (defaults
        to all of them).

        """
        paradigm_cell = parse_features(feature_string)

        violations = list(
            tuple(
                constraint(paradigm_cell, candidate)
                for constraint in self.constraints)
            for candidate in self.candidates)

        optimal = min(violations)

        strings = [
            [[render_featureset(paradigm_cell)]]
            + [[str(i)] for i in range(len(self.constraints))]]
        lineno = 0
        for profile, candidate in sorted(
                zip(violations, self.candidates),
                key=lambda x: x[0]):
            if max_lines is not None and lineno >= max_lines:
                break
            lineno += 1
            row = [['{}{}'.format(
                '\u2192' if profile == optimal else ' ',
                candidate)]]
            row.extend([str(v)] for v in profile)
            strings.append(row)

        return ascii_table(strings)

    def __str__(self):
        """Return string representation of a paradigm."""
        if self._filled is None:
            self._realise_cells()

        strings = [[['']] + [
            list(map(render_feature, sorted(col.items())))
            for col in self.columns]]

        for row_i, row in enumerate(self.filled):
            s_row = [[render_featureset(self.rows[row_i])]]
            for col in row:
                s_row.append([c.phon() for c in col])
            strings.append(s_row)

        return ascii_table(strings)


## Constraints ##

def match(paradigm_cell, candidate):
    """MATCH.

    Returns one violation for each mismatching feature between the paradigm cell
    and the candidate.

    """
    return sum(
        paradigm_cell[f] != candidate.features[f]
        for f in candidate.features)


def _general_ident(feature, paradigm_cell, candidate):
    if candidate.leading_form.features[feature] == candidate.features[feature]:
        return 0
    return 1

def ident(feature):
    """IDENT[F].

    Return a ident constraint for the feature F, which returns one violation,
    iff. the value for F in a candidate doesn't match the value in the
    corresponding leading form.

    """
    return partial(_general_ident, feature)


## Functions ##

def realise(constraints, candidates, paradigm_cell):
    """Return list of markers which are optimal for a paradigm cell.

    constraints:   Ordered list of constraints.
    candidates:    List of output candidates.
    paradigm_cell: Morpho-syntactic features of the morphological context.

    Constraints are functions which take a paradigm cell and a candidate as an
    argument and return an interger number of constraint violations.

    """
    optimal = None
    outputs = list()
    for candidate in candidates:
        violations = tuple(
            constraint(paradigm_cell, candidate)
            for constraint in constraints)

        if optimal is None or optimal > violations:
            optimal = violations
            outputs = list()
        if optimal == violations:
            outputs.append(candidate)

    return outputs
