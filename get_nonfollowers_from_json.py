import argparse
import json
from pathlib import Path
from sys import exit
from typing import Self

def parse_args():
    """Return: argparse argument object"""
    parser = argparse.ArgumentParser("get_nonfollowers_from_json")
    parser.add_argument("-i", "--input", type=str, required=True, help="Input directory to .json files")
    return parser.parse_args()

def main() -> int:
    """Prints all accounts that are not following back, after parsing a json dump of Instagram's following / followers data"""
    args = parse_args()
    input_path = Path(args.input)
    followers = ValueStorer().get_from_file(input_path / "followers_1.json", "followers")
    followings = ValueStorer().get_from_file(input_path / "following.json", "followings")
    PER_ROW, row_cntr, = 5, 0
    for following in followings.values: # Get set difference - only printing so loop to avoid store
        if following not in followers.values:
            print_newline = bool(row_cntr == PER_ROW-1)
            row_cntr = 0 if print_newline else row_cntr + 1
            print(following, end='\n' if print_newline else ', ')

class ValueStorer:
    """Used to create a set of all values with the json key 'value' - from the Instagram dump,
       seems that this covers both the followers & followings"""
    def __init__(self) -> Self:
        self.values: set[str] = set()

    def __call__(self, json_objs) -> None:
        for key, value in json_objs:
            if key.startswith("value"):
                self.values.add(value)
    
    def get_from_file(self, file_path: Path, desc: str) -> Self:
        file = raise_if_dne(file_path)
        json.load(file.open(), object_pairs_hook=self)
        if not self.values: raise RuntimeError(f"Cannot find any values for {desc}?")
        print(f"Found {len(self.values)} {desc}")
        return self

def raise_if_dne(path: Path) -> Path:
    if not path.exists(): raise RuntimeError(f"Path {path} does not exist")
    return path

if __name__ == "__main__":
    try:
        exit(main())
    except Exception as ex:
        print(f"Main exception - {ex}")
        exit(-1)