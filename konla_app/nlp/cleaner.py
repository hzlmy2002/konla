# class Cleaner:

#     def __init__(self, doc):
#         self.doc = doc




# import spacy
# from spacy.language import Language

# # https://www.youtube.com/watch?v=sp4B-JbEu7M
# @Language.component("adj_duplicates_removal")
# def adj_dup_removal(doc):
#     ents = list(doc.ents)
#     new_ents = []
#     for i in range(len(ents)):
#         if ents[i] != ents[i+1]:
#             new_ents.append(ents[i])
#     ents = tuple(new_ents)
#     doc.ents = ents
#     return (doc)

# Language.component("adj_duplicates_removal", func=adj_dup_removal)

#nlp.pipe_names
#nlp.add_pipe("adj_duplicates_removal")# class Cleaner:
#     """Cleaner Object used to preprocess the document"""

#     def __init__(self) -> None:
#         pass

#     def remove_adj_dupl_sents(doc):
#         """Remove duplicate adjacent sentences"""
#         text = []
#         for sent 
