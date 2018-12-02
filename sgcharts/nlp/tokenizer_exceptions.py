# coding: utf8
from __future__ import unicode_literals

_exc = {}
_exclude = ["Ill", "ill", "Its", "its", "Hell", "hell", "Shell", "shell",
            "Shed", "shed", "were", "Were", "Well", "well", "Whore", "whore"]

# Pronouns

for pron in ["i"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'m"] = [orth, "'m"]

        _exc[orth + "m"] = [orth, "m"]

        _exc[orth + "'ma"] = [orth, "'ma"]

        _exc[orth + "ma"] = [orth, "ma"]

for pron in ["i", "you", "he", "she", "it", "we", "they"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'ll"] = [orth, "'ll"]

        _exc[orth + "ll"] = [orth, "ll"]

        _exc[orth + "'ll've"] = [orth, "'ll've"]

        _exc[orth + "llve"] = [orth, "llve"]

        _exc[orth + "'d"] = [orth, "'d"]

        _exc[orth + "d"] = [orth, "d"]

        _exc[orth + "'d've"] = [orth, "'d've"]

        _exc[orth + "dve"] = [orth, "dve"]

for pron in ["i", "you", "we", "they"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'ve"] = [orth, "'ve"]

        _exc[orth + "ve"] = [orth, "ve"]

for pron in ["you", "we", "they"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'re"] = [orth, "'re"]

        _exc[orth + "re"] = [orth, "re"]

for pron in ["he", "she", "it"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'s"] = [orth, "'s"]

        _exc[orth + "s"] = [orth, "s"]

# W-words, relative pronouns, prepositions etc.

for word in ["who", "what", "when", "where", "why", "how", "there", "that"]:
    for orth in [word, word.title()]:
        _exc[orth + "'s"] = [orth, "'s"]

        _exc[orth + "s"] = [orth, "s"]

        _exc[orth + "'ll"] = [orth, "'ll"]

        _exc[orth + "ll"] = [orth, "ll"]

        _exc[orth + "'ll've"] = [orth, "'ll've"]

        _exc[orth + "llve"] = [orth, "llve"]

        _exc[orth + "'re"] = [orth, "'re"]

        _exc[orth + "re"] = [orth, "re"]

        _exc[orth + "'ve"] = [orth, "'ve"]

        _exc[orth + "ve"] = [orth, "ve"]

        _exc[orth + "'d"] = [orth, "'d"]

        _exc[orth + "d"] = [orth, "d"]

        _exc[orth + "'d've"] = [orth, "'d've"]

        _exc[orth + "dve"] = [orth, "dve"]

# Verbs

for verb_data in [
    "ca",
    "could",
    "do",
    "does",
    "did",
    "had",
    "may",
    "might",
    "must",
    "need",
    "ought",
    "sha",
    "should",
    "wo",
    "would"
]:
    verb_data_tc = verb_data.title()
    for orth in [verb_data, verb_data_tc]:
        _exc[orth + "n't"] = [orth, "n't"]

        _exc[orth + "nt"] = [orth, "nt"]

        _exc[orth + "n't've"] = [orth, "n't've"]

        _exc[orth + "ntve"] = [orth, "ntve"]

for verb_data in [
    "could",
    "might",
    "must",
    "should",
    "would",
]:
    verb_data_tc = verb_data.title()
    for orth in [verb_data, verb_data_tc]:
        _exc[orth + "'ve"] = [orth, "'ve"]

        _exc[orth + "ve"] = [orth, "ve"]

for verb_data in [
    "ai",
    "are",
    "is",
    "was",
    "were",
    "have",
    "has",
    "dare",
]:
    verb_data_tc = verb_data.title()
    for orth in [verb_data, verb_data_tc]:
        _exc[orth + "n't"] = [orth, "n't"]

        _exc[orth + "nt"] = [orth, "nt"]

# Other contractions with trailing apostrophe

for exc_data in [
    "doin",
    "goin",
    "nothin",
    "nuthin",
    "ol",
    "somethin"
]:
    exc_data_tc = exc_data.title()
    for orth in [exc_data, exc_data_tc]:
        _exc[orth] = [orth]
        _exc[orth + "'"] = [orth, "'"]

# Other contractions with leading apostrophe

for exc_data in [
    "cause",
    "em",
    "ll",
    "nuff"
]:
    exc_data_apos = "'" + exc_data
    for orth in [exc_data, exc_data_apos]:
        _exc[orth] = [orth]

# Times

for h in range(1, 12 + 1):
    for period in ["a.m.", "am"]:
        _exc["%d%s" % (h, period)] = ["%d" % h, period]
    for period in ["p.m.", "pm"]:
        _exc["%d%s" % (h, period)] = ["%d" % h, period]

# Rest

_other_exc = {
    "y'all": ["y", "'all"],

    "yall": ["y", "all"],

    "how'd'y": ["how", "'d", "'y"],

    "How'd'y": ["How", "'d", "'y"],

    "not've": ["not", "'ve"],

    "notve": ["not", "ve"],

    "Not've": ["Not", "'ve"],

    "Notve": ["Not", "ve"],

    "cannot": ["can", "not"],

    "Cannot": ["Can", "not"],

    "gonna": ["gon", "na"],

    "Gonna": ["Gon", "na"],

    "gotta": ["got", "ta"],

    "Gotta": ["Got", "ta"],

    "let's": ["let", "'s"],

    "Let's": ["Let", "'s"]
}

_exc.update(_other_exc)

for exc_data in [
    "'S",
    "'s",
    "\u2018S",
    "\u2018s",
    "and/or",
    "w/o",
    "'re",
    "'Cause",
    "'cause",
    "'cos",
    "'Cos",
    "'coz",
    "'Coz",
    "'cuz",
    "'Cuz",
    "'bout",
    "ma'am",
    "Ma'am",
    "o'clock",
    "O'clock",
    "lovin'",
    "Lovin'",
    "lovin",
    "Lovin",
    "havin'",
    "Havin'",
    "havin",
    "Havin",
    "doin'",
    "Doin'",
    "doin",
    "Doin",
    "goin'",
    "Goin'",
    "goin",
    "Goin",

    "Mt.",
    "Ak.",
    "Ala.",
    "Apr.",
    "Ariz.",
    "Ark.",
    "Aug.",
    "Calif.",
    "Colo.",
    "Conn.",
    "Dec.",
    "Del.",
    "Feb.",
    "Fla.",
    "Ga.",
    "Ia.",
    "Id.",
    "Ill.",
    "Ind.",
    "Jan.",
    "Jul.",
    "Jun.",
    "Kan.",
    "Kans.",
    "Ky.",
    "La.",
    "Mar.",
    "Mass.",
    "May.",
    "Mich.",
    "Minn.",
    "Miss.",
    "N.C.",
    "N.D.",
    "N.H.",
    "N.J.",
    "N.M.",
    "N.Y.",
    "Neb.",
    "Nebr.",
    "Nev.",
    "Nov.",
    "Oct.",
    "Okla.",
    "Ore.",
    "Pa.",
    "S.C.",
    "Sep.",
    "Sept.",
    "Tenn.",
    "Va.",
    "Wash.",
    "Wis."
]:
    _exc[exc_data] = [exc_data]

for orth in [
    "'d", "a.m.", "Adm.", "Bros.", "co.", "Co.", "Corp.", "D.C.", "Dr.", "e.g.",
    "E.g.", "E.G.", "Gen.", "Gov.", "i.e.", "I.e.", "I.E.", "Inc.", "Jr.",
    "Ltd.", "Md.", "Messrs.", "Mo.", "Mont.", "Mr.", "Mrs.", "Ms.", "p.m.",
    "Ph.D.", "Rep.", "Rev.", "Sen.", "St.", "vs."
]:
    _exc[orth] = [orth]

for string in _exclude:
    if string in _exc:
        _exc.pop(string)

TOKENIZER_EXCEPTIONS = _exc
