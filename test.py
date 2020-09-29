""" Simply look for a folder called "images" in the current directory and make sure it
is not empty. """

import pathlib

assert list((pathlib.Path.cwd() / "images").glob("*.jpg")), "No images found!"
