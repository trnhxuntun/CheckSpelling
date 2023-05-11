import pyvi
from pyvi import ViTokenizer

word = "sáng tác"
suggestions = pyvi.ViUtils.suggest_correction(word)
print(suggestions)