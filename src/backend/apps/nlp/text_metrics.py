import pandas as pd


class TextMetricsCalculator:

    # 200 based on https://infusion.media/content-marketing/how-to-calculate-reading-time/
    # 238 based on https://digest.bps.org.uk/2019/06/13/most-comprehensive-review-to-date-suggests-the-average-persons-reading-speed-is-slower-than-commonly-thought/
    READING_SPEED = 238  # wpm

    # Speaking time
    # - slow 110 wpm
    # - average 140 wpm
    # - fast 170 wpm
    SPEAKING_SPEED = 140  # wpm

    def _calculate_metrics(self, doc):
        words = [token.text for token in doc if not token.is_stop and not token.is_punct and token.text != '\n']
        res = dict()
        word_count = len(words)
        res["Word Count"] = word_count
        res["Character Count"] = sum([len(token.text) for token in doc])
        res["Reading Time (min)"] = str(word_count // self.READING_SPEED)
        res["Speaking Time (min)"] = word_count // self.SPEAKING_SPEED
        return res

    def get_metrics_html_table(self, doc):
        data = self._calculate_metrics(doc)
        df = pd.DataFrame(data, index=[0])
        return df.to_html(index=False)