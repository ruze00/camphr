"""
This type stub file was generated by pyright.
"""

import os

def add_codes(err_cls):
    """Add error codes to string messages via class attribute names."""
    class ErrorsWithCodes(object): ...

@add_codes
class Warnings(object):
    W001 = ...
    W002 = ...
    W003 = ...
    W004 = ...
    W005 = ...
    W006 = ...
    W007 = ...
    W008 = ...
    W009 = ...
    W010 = ...
    W011 = ...
    W012 = ...
    W013 = ...
    W014 = ...
    W015 = ...
    W016 = ...
    W017 = ...
    W018 = ...
    W019 = ...
    W020 = ...
    W021 = ...
    W022 = ...
    W023 = ...
    W024 = ...
    W025 = ...

@add_codes
class Errors(object):
    E001 = ...
    E002 = ...
    E003 = ...
    E004 = ...
    E005 = ...
    E006 = ...
    E007 = ...
    E008 = ...
    E009 = ...
    E010 = ...
    E011 = ...
    E012 = ...
    E013 = ...
    E014 = ...
    E015 = ...
    E016 = ...
    E017 = ...
    E018 = ...
    E019 = ...
    E020 = ...
    E021 = ...
    E022 = ...
    E023 = ...
    E024 = ...
    E025 = ...
    E026 = ...
    E027 = ...
    E028 = ...
    E029 = ...
    E030 = ...
    E031 = ...
    E032 = ...
    E033 = ...
    E034 = ...
    E035 = ...
    E036 = ...
    E037 = ...
    E038 = ...
    E039 = ...
    E040 = ...
    E041 = ...
    E042 = ...
    E043 = ...
    E044 = ...
    E045 = ...
    E046 = ...
    E047 = ...
    E048 = ...
    E049 = ...
    E050 = ...
    E051 = ...
    E052 = ...
    E053 = ...
    E054 = ...
    E055 = ...
    E056 = ...
    E057 = ...
    E058 = ...
    E059 = ...
    E060 = ...
    E061 = ...
    E062 = ...
    E063 = ...
    E064 = ...
    E065 = ...
    E066 = ...
    E067 = ...
    E068 = ...
    E069 = ...
    E070 = ...
    E071 = ...
    E072 = ...
    E073 = ...
    E074 = ...
    E075 = ...
    E076 = ...
    E077 = ...
    E078 = ...
    E079 = ...
    E080 = ...
    E081 = ...
    E082 = ...
    E083 = ...
    E084 = ...
    E085 = ...
    E086 = ...
    E087 = ...
    E088 = ...
    E089 = ...
    E090 = ...
    E091 = ...
    E092 = ...
    E093 = ...
    E094 = ...
    E095 = ...
    E096 = ...
    E097 = ...
    E098 = ...
    E099 = ...
    E100 = ...
    E101 = ...
    E102 = ...
    E103 = ...
    E104 = ...
    E105 = ...
    E106 = ...
    E107 = ...
    E108 = ...
    E109 = ...
    E110 = ...
    E111 = ...
    E112 = ...
    E113 = ...
    E114 = ...
    E115 = ...
    E116 = ...
    E117 = ...
    E118 = ...
    E119 = ...
    E120 = ...
    E121 = ...
    E122 = ...
    E123 = ...
    E124 = ...
    E125 = ...
    E126 = ...
    E127 = ...
    E128 = ...
    E129 = ...
    E130 = ...
    E131 = ...
    E132 = ...
    E133 = ...
    E134 = ...
    E135 = ...
    E136 = ...
    E137 = ...
    E138 = ...
    E139 = ...
    E140 = ...
    E141 = ...
    E142 = ...
    E143 = ...
    E144 = ...
    E145 = ...
    E146 = ...
    E147 = ...
    E148 = ...
    E149 = ...
    E150 = ...
    E151 = ...
    E152 = ...
    E153 = ...
    E154 = ...
    E155 = ...
    E156 = ...
    E157 = ...
    E158 = ...
    E159 = ...
    E160 = ...
    E161 = ...
    E162 = ...
    E163 = ...
    E164 = ...
    E165 = ...
    E166 = ...
    E167 = ...
    E168 = ...
    E169 = ...
    E170 = ...
    E171 = ...
    E172 = ...
    E173 = ...
    E174 = ...
    E175 = ...
    E176 = ...
    E177 = ...
    E178 = ...
    E179 = ...
    E180 = ...
    E181 = ...
    E182 = ...
    E183 = ...
    E184 = ...
    E185 = ...
    E186 = ...
    E187 = ...

@add_codes
class TempErrors(object):
    T003 = ...
    T004 = ...
    T007 = ...
    T008 = ...

class MatchPatternError(ValueError):
    def __init__(self, key, errors):
        """Custom error for validating match patterns.

        key (unicode): The name of the matcher rule.
        errors (dict): Validation errors (sequence of strings) mapped to pattern
            ID, i.e. the index of the added pattern.
        """
        ...

class AlignmentError(ValueError): ...
class ModelsWarning(UserWarning): ...

WARNINGS = {
    "user": UserWarning,
    "deprecation": DeprecationWarning,
    "models": ModelsWarning,
}

def _get_warn_types(arg): ...
def _get_warn_excl(arg): ...

SPACY_WARNING_FILTER = os.environ.get("SPACY_WARNING_FILTER")
SPACY_WARNING_TYPES = _get_warn_types(os.environ.get("SPACY_WARNING_TYPES"))
SPACY_WARNING_IGNORE = _get_warn_excl(os.environ.get("SPACY_WARNING_IGNORE"))

def user_warning(message): ...
def deprecation_warning(message): ...
def models_warning(message): ...
def _warn(message, warn_type=...):
    """
    message (unicode): The message to display.
    category (Warning): The Warning to show.
    """
    ...
