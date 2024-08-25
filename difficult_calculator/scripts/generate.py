import json
from gendiff import generate_diff

diff = generate_diff(json.load(open('../files/file1.json')),
                     json.load(open('../files/file2.json')))
#'difficult_calculator/files/file1.json' 'difficult_calculator/files/file2.json'
print(diff)