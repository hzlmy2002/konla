import pandas as pd

class BasicNamedEntityRecognizer:
    """Saves named entities in a pandas dataframe"""

    def __init__(self, doc):
        d = []
        for entity in doc.ents:
            d.append((entity.label_, entity.text))
        self.df = pd.DataFrame(d, columns=('named entity', 'output'))

    def get_html_table(self):
        return self.df.to_html()