import spacy
# Written by Bartosz Grabek 
# eg. '1 Introduction \n', note: will not match lowercase stopwords
heading_pattern_strict = [
    {"ORTH": "\n", "OP": "+"},
    {"IS_DIGIT": True},
    {"ORTH": ".", "OP": "?"},
    {"IS_TITLE": True, "OP":"+"},
    {"ORTH": "\n", "OP": "+"}
]

""" heading_pattern_loose may match in-section text
this problem is partially resolved through
checking letter case after matching """
heading_pattern_loose = [
    {"ORTH": "\n", "OP": "+"}, # 
    {"IS_DIGIT": True},
    {"ORTH": ".", "OP": "?"},
    {"IS_ALPHA": True, "OP":"+"},
    {"ORTH": "\n", "OP": "+"}
]

# eg. '4.2 Summary'# eg. '4.2 Summary'
# works similarly to heading_pattern_loose
subheading_pattern_loose = [
    {"ORTH": "\n", "OP": "+"}, # 
    {"TEXT": {"REGEX": "[0-9]+\.[0-9]+"}},
    {"ORTH": ".", "OP": "?"},
    {"IS_ALPHA": True, "OP": "+"},
    {"ORTH": "\n", "OP": "+"}
]
subheading_pattern_loose_ascii = [
    {"ORTH": "\n", "OP": "+"}, # 
    {"TEXT": {"REGEX": "[0-9]+\.[0-9]+"}},
    {"ORTH": ".", "OP": "?"},
    {"IS_ASCII": True, "OP": "+"},
    {"ORTH": "\n", "OP": "+"}
]

# Reference Section Pattern Matching
ref_section = [
    {"ORTH": "\n", "OP": "+"},
    {"TEXT": {"REGEX": "[0-9]"}, "OP": "?"},
    {"ORTH": ".", "OP":"?"},
    {"LOWER": {"IN": ["references", "bibliography"]}},
    {"ORTH": "\n", "OP": "+"}
]

class SectionExtractor():
    """
    Acquires the ranges of text for each matched section and subsection.
    If text segmentation follows standard enumaration, 1., 1.1., 1.2, 1.3, etc.,
    it discerns ranges for sections and subsections.
    First section title that does not follow the numbering will include the last
    token of the previous section. Last section is cutoff at first token of 
    reference section if found, otherwise the last token of text.
    """
    def __init__(self, doc, nlp):
        self.doc = doc  # doc must be the result of applying spacy lang model to raw text
        self.nlp = nlp  # model
        self.segments = []
        self.refs = []  # holds titles for reference sections
        self.refs_start_tk = len(doc)  # start tk of reference section, default end of doc

    def _get_matches(self):
        matcher = spacy.matcher.Matcher(self.nlp.vocab)
        matcher.add("heading_strict", [heading_pattern_strict])
        matcher.add("heading_loose", [heading_pattern_loose])
        matcher.add("subheading_loose", [subheading_pattern_loose])
        matcher.add("subheading_loose_ascii", [subheading_pattern_loose_ascii])
        matcher.add("reference_section", [ref_section])
        return matcher(self.doc)

    def _check_matches(self, matches):
        """
        Returns a list of all valid matches in a 4-tuple form:
        (match_text, match_string_id, match_start_tk, match_end_token)
        eg. ("1. Introduction \n", "heading_strict", 52, 55)
        Excludes sections labeled matched by 'reference_section' pattern
        """
        matched = []
        for match_id, start, end in matches:
            string_id = self.nlp.vocab.strings[match_id]
            span = self.doc[start:end]
            match_text = span.text
            if string_id == "reference_section":
                self.refs.append(match_text)
                self.refs_start_tk = min([start, self.refs_start_tk])
            else:  # check if non-reference for recognized as sections
                if not(match_text in self.refs):
                    # check if all non-stopwords are capitalized or upper (use if loose patterns)
                    valid = True
                    for tk in span:
                        if not(tk.like_num or tk.is_stop or tk.is_punct or tk.is_digit or tk.is_space):
                            valid = tk.is_title or tk.is_upper
                            if valid == False:
                                break
                    # check if no \n chars in match
                    for tk in span[1:-2]:
                        if tk.text == "\n":
                            valid = False
                    if valid:
                        matched.append((match_text, string_id, start, end))
        return matched
    
    def _remove_copies_and_overlap(self, matched):
        """Removes duplicated or overlapping matches based on order and length"""
        final = []
        final.append(matched.pop(0)) # first 4-tuple
        for m in matched:
            last = final[-1]  # get last section
            if m[2] <= last[2]:  # if m.start_tk <= last.start_tk
                if m[3]-m[2] > last[3]-last[2]:  # if len(m) > len(last)
                    final.pop()  # remove last section
                    final.append(m)  # replace it with new section
            else:
                final.append(m) # add new section    
        return final
    
    def _get_section_ranges(self, final):
        """ 
        Returns a list containing 4-tuples:
        (section_name, section_start_tk, section_end_tk, length_in_tokens)
        """
        # strip match.text to check for possible section range
        final = [(f[0].strip(),f[1],f[2],f[3]) for f in final]
        ranges = []
        for i in range(len(final)-1):
            section_now = final[i]
            start = section_now[3]+1           # section_now.end_tk + 1
            num_1 = section_now[0].split()[0]  # get section order num, eg. 3, 3.2, 5., 7.2.
            section_next = final[i+1]
            num_2 = section_next[0].split()[0]
            # start checking following sections
            j = i+1
            take_end_of_doc = False
            while num_2.startswith(num_1): # eg. '1.4' follows section '1.'
                j += 1
                if j > len(final)-1:
                    take_end_of_doc = True
                    break
                section_next = final[j]
                num_2 = section_next[0].split()[0]  # take next section order num
            if not take_end_of_doc:
                end = section_next[2]-1  # section_next.start_tk - 1
            else:
                end = len(self.doc)  # take last token number
            # Append (section_name, start_tk, end_tk, length_in_tokens)
            ranges.append((section_now[0], start, end, end-start))
        # Append last section, cutoff at refs_start_tk
        last_sec = final[-1]
        ranges.append((last_sec[0], last_sec[3], self.refs_start_tk, self.refs_start_tk-last_sec[3]))
        return ranges

    def run(self):
        matches = self._get_matches()
        matches = self._check_matches(matches)
        matches = self._remove_copies_and_overlap(matches)
        self.segments = self._get_section_ranges(matches)
        return self.segments