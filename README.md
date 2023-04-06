# Private data tokenizator
Script replaces all text private data, such as named entities, dates, money sums into a tokens.

# Requirments
- Python
- Pip

# Installation
## For Linux
- /.init.sh
## For Windows
- pip install -U pip setuptools wheel
- pip install -U spacy
- python -m spacy download en_core_web_sm
- create file decrypted.txt: "type nul > decrypted.txt"
- create file encrypted.json: "type nul > encrypted.json"

# Supported languages
- English

# How to use
- Paste text with private info into decrypted.txt
- Run encrypt script
```
python encrypt.py
```
- encrypted.json will have encription data in such structure
```
{
  "unserialize_hash": string,
  "content": string
}
```
- copy "content" property value

- use at at ChatGpt
```
I will provide you text filled with encoded nouns, which you can misconfuse with random strings. You should relate to those as nouns which can be names, dates or number. I need you to summarize document statements. Use codes in answer as usual nouns in your answer, without any formatting or quotes. Leave no notes or additional comments. Show result as a list.
Text:
Content goes here
```

- Run decrypt script
```
python decrypt.py
```
- Find unecripted data in decrypted.txt 
