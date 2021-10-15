from conllulex.supersenses import NSS, VSS, PSS


def supersenses_for_lexcat(lc):
    if lc == "N":
        return NSS
    if lc == "V" or lc.startswith("V."):
        if lc != "V":
            assert lc in {
                "V.VID",
                "V.VPC.full",
                "V.VPC.semi",
                "V.LVC.full",
                "V.LVC.cause",
                "V.IAV",
            }, lc  # PARSEME 1.1 verbal MWE subtypes
        return VSS
    if lc in ("P", "PP", "INF.P"):
        return PSS
    if lc in ("POSS", "PRON.POSS"):
        return PSS | {"`$"}


ALL_LEXCATS = {
    "N",
    "PRON",
    "V",
    "P",
    "PP",
    "INF",
    "INF.P",
    "POSS",
    "PRON.POSS",
    "DISC",
    "AUX",
    "ADJ",
    "ADV",
    "DET",
    "CCONJ",
    "SCONJ",
    "INTJ",
    "NUM",
    "SYM",
    "PUNCT",
    "X",
}
