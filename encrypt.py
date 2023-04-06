import utils.constants as constants
import utils.object_serialization as object_serialization
from utils.get_random_string import get_random_string

import json
import spacy
nlp = spacy.load('en_core_web_sm')

print('Reading {} content'.format(constants.INPUT_FILE_NAME))
doc_string = ''
with open(constants.INPUT_FILE_NAME) as file:
    doc_string = file.read()

print('Figuring out private names and numbers')
doc = nlp(doc_string)

print('Tokenizing private data in text')
token_dictionary = {}
tokenized_string = ""

last_processed_character_index = 0
for ent in doc.ents:
    tokenized = get_random_string(16)
    token_dictionary[tokenized] = ent.text
    tokenized_string += doc_string[last_processed_character_index:ent.start_char] + tokenized
    last_processed_character_index = ent.end_char

print('Writing result to {}'.format(constants.OUTPUT_FILE_NAME))
token_dictionary_hash = object_serialization.serialize_array(token_dictionary)
with open(constants.OUTPUT_FILE_NAME, 'w') as outfile:
    outfile.write(
        json.dumps({
            constants.UNSERIALIZE_HASH: token_dictionary_hash,
            constants.CONTENT: tokenized_string
        })
    )

print('Done.')
