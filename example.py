import json
import sys
from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer

with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

    djv =  Dejavu(config)
    if len(sys.argv) != 2:
        print("Usage: python script.py argument")
        sys.exit(1)

    # Get the argument passed
    argument = sys.argv[1]
    #fingerprint mp3 in our directories
   # djv.fingerprint_directory("raw", [".mp3", ".wav"])
    results = djv.recognize(FileRecognizer, argument)
    for i in results['results']:
        print(f"song name: {i['song_name']}, input_confindence: {i['input_confidence']}, fingerprinted_confidence: {i['fingerprinted_confidence']}" )

