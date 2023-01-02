import argparse
import json
import os
import re
import shlex
import subprocess

import requests
from deepdiff import DeepDiff

# Recipe file regular expressions
JSON_RE = re.compile(r"\*\*JSON-LD:? ?(?P<type>[A-Za-z ]*) ?(?P<number>\d*)?.*:?\*\* *\| \[(?P<url>.*)\]")
PYTHON_RE = re.compile(r'--8<-- "(?P<loc>.*-(?P<method>method\d+)-?(?P<type>\w*)?.*\.py)"')


def build_json_dict(matches):
    result = {}
    for match in matches:
        flat = f"{match.group('type').replace(' ','').lower()}{match.group('number')}"
        if flat == "":
            flat = "general"
        if flat in result:
            result[flat]["json"].append(match.group('url'))
        else:
            result[flat] = {"json": [match.group('url')]}
    return result


def get_json(json_file):
    # Flatten the directory name of the Cookbook recipe into the target filename
    flat = "-".join(json_file.split("/")[-2:])
    json_path = f"{args.cache_directory}/{flat}"

    # Download the file if necessary
    if args.ignore_cache or not os.path.exists(json_path):
        response = requests.get(json_file)
        if response.status_code == 200:
            with open(json_path, "wb") as out:
                out.write(response.content)
        else:
            print(f"ERROR: Could not download {json_file} - Status Code {response.status_code}")
            return None

    # Parse and return the JSON
    try:
        json_data = json.load(open(json_path, 'r'))
        return json_data
    except Exception as e:
        print(f"ERROR: Could not parse JSON from {json_path} - {e}")
        return None


def run_test(python_file, json_file):
    # Get the target JSON from cache or download
    target = get_json(json_file)
    if not target:
        return False

    # Run the Python script, catch the output and try and parse the JSON
    try:
        output = subprocess.run(shlex.split(f"python ../{python_file}"), capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Running script {python_file} - {e}")
        return False

    try:
        j = json.loads(output.stdout)
    except json.JSONDecodeError as e:
        print(f"ERROR: Could not parse valid JSON from output of script {python_file} - {e}")
        return False

    # Diff the generated JSON against the target
    result = DeepDiff(target, j)
    if result == {}:
        return True
    else:
        print(f"FAILURE: The output of script {python_file} did not match the Cookbook JSON {json_file}")
        if args.verbose >= 1:
            print("===Differences===")
            print(result)
            print("=================")
        return False


def process_recipe(file):  # noqa: C901
    results = []

    # Sanity check the file
    if not file.endswith(".md"):
        print(f"ERROR: {file} does not have a .md extension")
        return False

    # Read recipe file
    try:
        recipe_data = open(file, "r").read()
    except Exception as e:
        print(f"ERROR: Could not read {file} - {e}")
        return False

    # Find JSON-LD and Python links
    json_links = JSON_RE.finditer(recipe_data)
    python_links = PYTHON_RE.finditer(recipe_data)

    # Convert JSON files into a dictionary for type matching
    json_dict = build_json_dict(json_links)

    # Walkthrough each Python link found and try to match it to a JSON file
    for p in python_links:
        t = p.group('type')
        if t == "":
            t = "general"
        if t in json_dict:
            if "python" in json_dict[t]:
                json_dict[t]["python"].append(p.group('loc'))
            else:
                json_dict[t]["python"] = [p.group('loc')]
        else:
            if args.fail_missing:
                print(f"ERROR: {p.group('loc')} could not be matched to a Cookbook JSON in {file}")
                return False
            else:
                if args.verbose >= 1:
                    print(f"WARNING: {p.group('loc')} could not be matched to a Cookbook JSON in {file}")

    # Check all the JSON file groups have associated scripts and run them
    for t in json_dict:
        if "python" not in json_dict[t]:
            if args.fail_missing:
                print(f"ERROR: JSON group {t} does not have any associated Python scripts in {file}")
                return False
            else:
                if args.verbose >= 1:
                    print(f"WARNING: JSON group {t} does not have any associated Python scripts in {file}")

        else:
            # Loop the JSON files and run each associated test script
            for j in json_dict[t]["json"]:
                for p in json_dict[t]["python"]:
                    result = run_test(p, j)
                    results.append(result)

                    # Fail out if necessary
                    if not result and args.fail_fast:
                        exit(1)

    return all(results)


if __name__ == "__main__":
    global args

    parser = argparse.ArgumentParser()
    parser.add_argument('recipe_file', nargs="+", help="The recipe(s) to test")
    parser.add_argument('-v', "--verbose", action="count", default=0, help="Increase output verbosity")
    parser.add_argument("-y", action="store_true", help="Bypass 'Are you sure?' question")
    parser.add_argument("--ignore-cache", action="store_true", help="Always download Cookbook JSON files")
    # parser.add_argument("--no-cache", action="store_true", help="Remove Cookbook JSON files after use")
    parser.add_argument("--fail-fast", action="store_true", help="Fail the whole run as soon as one test fails")
    parser.add_argument("--fail-missing", action="store_true", help="Fail an individual recipe if any of the JSON files are missing implementations in code or any of the Python files can't be matched to a Cookbook JSON")
    parser.add_argument("--cache-directory", type=str, help="Cache directory for Cookbook JSON files (default: .cache)", default=".cache")
    args = parser.parse_args()
    # print(args)

    # Perform security check
    if not args.y:
        response = input("This script will execute what could be arbitrary Python code from files in the docs/recipes/scripts directory. Are you sure you want to continue? (y/n) ")
        if response.lower() != "y":
            exit()

    results = []

    # Make the cache directory if it does not exist
    os.makedirs(args.cache_directory, exist_ok=True)

    # Check the validity of the input files and call the runner
    for file in args.recipe_file:
        if not os.path.isfile(file):
            print(f"ERROR: file {file} does not exist")
            exit(1)

        result = process_recipe(file)
        results.append(result)

        if not result and args.fail_fast:
            exit(1)

    if not all(results):
        exit(1)
    else:
        exit(0)
