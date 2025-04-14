# MIT License
#
# Copyright (c) 2025 Rodney M. Maniego Jr.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import glob
import json
import shutil
import random

import numpy as np

DST = "data"
SHEAR1 = "source/shear"
NO_SHEAR1 = "source/no-shear"
SHEAR2 = "target/shear"
NO_SHEAR2 = "target/no-shear"


def _get_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def _preprocess_target(target):
    """ """

def main():
    """ """
    global DST
    global NO_SHEAR1
    
    print(f"\n[{NO_SHEAR1}]")
    targets = glob.glob(f"{DST}/{NO_SHEAR1}/*.json")
    for filepath in targets:
        print(f" * {filepath}")

        matrix = np.zeros((161, 141)).tolist()
        destination = filepath.replace(NO_SHEAR1, NO_SHEAR2)
        destination = destination.replace("wind_data_925hPa", "")
        with open(destination, "w", encoding="utf-8") as file:
            json.dump(matrix, file, indent=4)

    _preprocess_target(NO_SHEAR1)

if __name__ == "__main__":
    main()
