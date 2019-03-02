from nltk.stem import WordNetLemmatizer
import re

def lemmatize(w: str):
  """
  Improved lemmatizer based on nltk.stem.WordNetLemmatizer
  """
  if w in {'as', 'us', 'ms', 'mrs', 'vs', 'cos', 'wis', 'mis',
           'des', 'les', 'las', 'pas', 'der', 'es', 'est',
           'during', 'feed', 'mater',
           'ground', 'clad', 'unclad',
           'ss', 'os', 'hs', 'ps', 'cs', 'rs', 'bs', 'ds', 'fs', 'gs',
           'js', 'ks', 'ls', 'ns', 'qs', 'rs', 'ts', 'xs', 'ys', 'zs',
           'lest', 'lester', 'kester', 'vester', 'mester',
           'kest', 'cest', 'cester', 'dester'}:
    return w

  if w in {'bees', 'axes'}:
    return w[:-1]

  """ match open syllables 'consonate + vowel + consonate + e' """
  match_op = re.match(
      r'^([pbtdfvlmnghkczrwsx]{1,3})([aiou])([pbtdfvlmngkhczr])(es|ed|ing|ings)$', w)
  if match_op:
    return f'{match_op[1]}{match_op[2]}{match_op[3]}e'

  """ match ending 'ss' """
  match_ss = re.match(r'^([a-z]*)([aeiou])(ss)(es|ed|er|ing)?s?$', w)
  if match_ss:
    return f'{match_ss[1]}{match_ss[2]}{match_ss[3]}'

  wnl = WordNetLemmatizer()
  stub = wnl.lemmatize(w, pos='r')  # ADV
  stub = wnl.lemmatize(stub, pos='a')  # ADV
  stub = wnl.lemmatize(stub, pos='v')  # VERB
  stub = wnl.lemmatize(stub, pos='n')  # NOUN
  return stub
