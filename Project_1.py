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


# if __name__ == '__main__':
#     print(extract_text_from_pdf('test5.pdf'))

# import spacy
import spacy

from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en')

# Extracted PDF file to Text
pdftext = extract_text_from_pdf('test5.pdf')

# Runs extracted text through NLP (Natural Language Processor)
doc = nlp(pdftext)

core_patterns = [nlp(text) for text in ('drug', 'overdose')]
peripheral_patterns = [nlp(text) for text in ('death', 'problem')]
# material_patterns = [nlp(text) for text in ('silk', 'yellow fabric')] (COULD HAVE ONE FOR NUMBERS?)

matcher = PhraseMatcher(nlp.vocab)
matcher.add('CORE', None, *core_patterns)
matcher.add('PERIPHERAL', None, *peripheral_patterns)
# matcher.add('MATERIAL', None, *material_patterns)

matches = matcher(doc)
for match_id, start, end in matches:
    rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'COLOR'
    span = doc[start : end]  # get the matched slice of the doc
    print(rule_id, span.text)
