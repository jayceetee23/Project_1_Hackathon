# spaCy Library Demonstration

Code demonstrates some uses with spaCy library. Spacy is a open-source library for Natural Language Processing in Python. The goal is to extract text from a .pdf file to use with the spacy library.

Here we use the library pdf miner in order to extract the text from the .pdf file and convert it into workable text. 
![pdfMiner Image](https://user-images.githubusercontent.com/47049525/56011997-f7ec4700-5caf-11e9-92ea-e7290e96bdc4.PNG)

We then import spacy and load the English tokenizer, tagger, parser, NER and word vectors. Phrase matcher allows us to add key words to the terminology list. While parsing through the extracted text, if any of the 'key words' in the terminology list appear, we record the number of times that specific word appears through the text.
![spacy1](https://user-images.githubusercontent.com/47049525/56012008-08042680-5cb0-11e9-9a6f-60ed39e8b5de.PNG)
![spacy2](https://user-images.githubusercontent.com/47049525/56012013-105c6180-5cb0-11e9-9fa5-cdee427ba4f5.PNG)
![word numbers](https://user-images.githubusercontent.com/47049525/56012026-1e11e700-5cb0-11e9-9d78-69204a3ce2af.PNG)

![noun and verb output](https://user-images.githubusercontent.com/47049525/56012021-16ead900-5cb0-11e9-82f3-d9caf190e5f9.PNG)


![Sentences](https://user-images.githubusercontent.com/47049525/56012036-236f3180-5cb0-11e9-9eda-cc80583d3435.PNG)
