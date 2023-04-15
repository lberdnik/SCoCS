ONE_WORD_ABREBIATION = [
    "dr.", "esq.", "hon.", "jr.", "mr.", "mrs.", "ms.", "messrs.", "mmes.",
    "msgr.", "prof.", "rev.", "sr.", "st.", "jan.", "feb.", "mar.", "apr.", 
    "jun.", "jul.", "aug.", "sep.", "sept.", "oct.", "nov.", "dec.", "mon.", 
    "tu.", "tue.", "tues.", "wed.", "th.", "thu.", "thur.", "thur.", "thurs.", 
    "fri.", "sat.", "sun.", "in.", "lbs.", "adv.", "eng.", "asst.", "corp.", 
    "ave.", "trans.", "gen.", "maj.", "hon.", "jer.", "pres.", "st.", "co.", 
    "brig.", "inc.", "ltd."]

TWO_WORDS_ABREBIATION = [
    "b.a.", "ph.d.", "m.a.", "e.g.", "p.m.", "a.m.", "U.K", "t.p.", "v.t"]

THREE_WORDS_ABREBIATION = ["v.i.p.", "p.p.s."]

SENTENCE_PATTERN = r"[.!?\"]+"
NON_DECLARATIVE_PATTERN = r"[!?]+"
WORD_PATTERN = r"\w*[a-zA-Z]\w*"
NUMBER_PATTERN = r"\b[0-9]+\b\s*"
DIRECT_SPEECH_PATTERN = r"[\"]([^\"]+)[\"]"