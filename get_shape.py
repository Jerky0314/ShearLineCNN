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


SHEAR1 = "data/source/shear"
NO_SHEAR1 = "data/source/no-shear"
SHEAR2 = "data/target/shear"
NO_SHEAR2 = "data/target/no-shear"


def _get_shear_line(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def main():
    """ """

    global DATASET
    global TARGETS
    global SHEAR1
    global SHEAR2
    global NO_SHEAR1
    global NO_SHEAR2

    targets = glob.glob(f"{SHEAR1}/*.json")
    for target in targets:
        
        data = _get_shear_line(target)
        matrix = np.array(data)
        
        print(matrix.shape)
        break

if __name__ == "__main__":
    main()
