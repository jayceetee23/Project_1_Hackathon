# spaCy Library Demonstration

Code demonstrates some uses with spaCy library. Spacy is a open-source library for Natural Language Processing in Python. The goal is to extract text from a .pdf file to use with the spacy library.

Here we use the library pdf miner in order to extract the text from the .pdf file and convert it into workable text. 
![pdfMiner Image](https://user-images.githubusercontent.com/47049525/56011997-f7ec4700-5caf-11e9-92ea-e7290e96bdc4.PNG)

We then import spacy and load the English tokenizer, tagger, parser, NER and word vectors. Phrase matcher allows us to add key words to the terminology list. While parsing through the extracted text, if any of the 'key words' in the terminology list appear, we record the number of times that specific word appears through the text.
![spacy1](https://user-images.githubusercontent.com/47049525/56012008-08042680-5cb0-11e9-9a6f-60ed39e8b5de.PNG)
![code terminology](https://user-images.githubusercontent.com/47049525/56012376-dc823b80-5cb1-11e9-8f70-1ee7464dd7a5.PNG)
![word numbers](https://user-images.githubusercontent.com/47049525/56012026-1e11e700-5cb0-11e9-9d78-69204a3ce2af.PNG)

Here we parse through the text document and output noun phrases that appear through the text. We apply the same tokenization with verbs that also appear in the text.

![Capture](https://user-images.githubusercontent.com/47049525/56012450-2539f480-5cb2-11e9-9596-37fc11b47c2e.PNG)
![noun and verb output](https://user-images.githubusercontent.com/47049525/56012021-16ead900-5cb0-11e9-82f3-d9caf190e5f9.PNG)

With spacy we are able to separate the text into sentences based on puncuation marks that end the sentences (. or ! or ?). Although this works well with the text, issues do arise when going through numerical data such as charts or graphs (as seen in the output).
![Sentences](https://user-images.githubusercontent.com/47049525/56012036-236f3180-5cb0-11e9-9eda-cc80583d3435.PNG)
