import string
from zhon.hanzi import punctuation
tweet = "I am tired! 草泥马，sdpsjcojahcp"
translator = str.maketrans(punctuation, ' '*len(punctuation)) #map punctuation to space
print(tweet.translate(translator))