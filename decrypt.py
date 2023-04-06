import utils.constants as constants
import utils.object_serialization as object_serialization
import json
import sys

print('Reading {} content'.format(constants.OUTPUT_FILE_NAME))
output_file_string = ""
with open(constants.OUTPUT_FILE_NAME) as file:
    lines = file.readlines()

    for index, line in enumerate(lines):
        if (index != 0):
            output_file_string += "\\n"
        output_file_string += line.strip() 

print('Checking necessary data for decryption')
output_file_object = json.loads(output_file_string)
if not all(name in output_file_object for name in [constants.UNSERIALIZE_HASH, constants.CONTENT]):
    print('{} should have following structure to be decrypted:'.format(constants.OUTPUT_FILE))
    print('{{"{}": string, "{}": string}}'.format(constants.UNSERIALIZE_HASH, constants.CONTENT))
    sys.exit()

token_dictionary = object_serialization.deserialize_array(output_file_object[constants.UNSERIALIZE_HASH])
content = output_file_object[constants.CONTENT]

print('Decrypting content')
for token, word in token_dictionary.items():
    content = content.replace(token, word)

print('Writing decrypted result to {}'.format(constants.INPUT_FILE_NAME))
with open(constants.INPUT_FILE_NAME, "w") as outfile:
    outfile.write(content)

print('Done.')
