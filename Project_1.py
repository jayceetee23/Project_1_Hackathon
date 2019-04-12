import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

# PDF Miner extracts text from .pdf file and converts contents to text
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text


if __name__ == '__main__':
    print(extract_text_from_pdf('test5.pdf'))

# import spacy library
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en')


pdftext = extract_text_from_pdf('test5.pdf')

# import PhraseMatcher
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

# Phrases (or words) that are a part of the terminology_list
terminology_list = [u"drug", u"overdose", u"death"]

patterns = [nlp.make_doc(text) for text in terminology_list]
matcher.add("TerminologyList", None, *patterns)

doc = nlp(pdftext)

matches = matcher(doc)

drug_count = 0
overdose_count = 0
death_count = 0

# Counter for number of times a word in the terminology_list matches the pattern in the text document
for match_id, start, end in matches:
    span = doc[start:end]
    # print(span.text)

    if span.text == "drug":
        drug_count = drug_count + 1
    elif span.text == "overdose":
        overdose_count = overdose_count + 1
    elif span.text == "death":
        death_count = death_count + 1

# Print counts for words: 'drug', 'overdose', 'death'
print("Number of times text 'drug' appears in article: ", drug_count)
print("Number of times text 'overdose' appears in article: ", overdose_count)
print("Number of times text 'death' appears in article: ", death_count)

print("\n")

# Tokenization: Print noun phrases that appear in text document
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])

# Tokenization: Print Verbs that appear in text document
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Separate text into sentences
for entity in doc.sents:
    print(entity.text, entity.label_, "\n")
