import pandas as pd
import wordbook

dataset = pd.DataFrame(
    {'word': ['simple', 'hard', 'middle'], 'freq': ['W1', 'W2', 'W3']})

print(wordbook.generate_html(dataset))

wordbook.create_book() #This will create a html on your desktop with the sample file.
