'''
    Some tests for the generated degraded JSON format with offset annotations
'''

import os
import argparse
import json
from collections import OrderedDict

files = ["PMC5271396.json", "PMC5271396.json", "PMC4987885.json"]

def test_corpus(path_json_repo):
    for file in files:
        print(os.path.join(path_json_repo, file))
        with open(os.path.join(path_json_repo, file)) as jsonfile:
            json_doc = json.load(jsonfile, object_pairs_hook=OrderedDict)

        for paragraph in json_doc["body_text"]:
            text = paragraph["text"]
            entities = None
            references = None
            if "entity_spans" in paragraph:
                entities = paragraph["entity_spans"] 
            if "ref_spans" in paragraph:
                references = paragraph["ref_spans"]

            if entities is not None:
                for entity in entities:
                    entity_str = entity["rawForm"]
                    entity_text = text[entity["start"]:entity["end"]]
                    print(entity_str)
                    if entity_str != entity_str:
                        print(entity_str, entity_str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description = "Test degraded JSON format")
    parser.add_argument("--json-repo", type=str, 
        help="path to the directory of JSON files converted from TEI XML produced by GROBID and used in the Softcite corpus")

    args = parser.parse_args()
    json_repo = args.json_repo

    # check path and call methods
    if json_repo is not None and not os.path.isdir(json_repo):
        print("the path to the JSON files is not valid: ", json_repo)

    test_corpus(json_repo)