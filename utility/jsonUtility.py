import json
import os


def getFilePath(payloadFileName):
    current_directory = os.getcwd()
    return os.path.join(current_directory, "payloads", f"{payloadFileName}.json")


def getJsonData(payloadFileName):
    json_file_path = getFilePath(payloadFileName)
    with open(json_file_path, "r") as json_file:
        return json.load(json_file)