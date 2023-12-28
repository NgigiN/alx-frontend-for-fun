#!/usr/bin/python3
"""
	This script is used to convert markdown to html. It takes 2 arguments.
	1. markdown file
	2. html file
    Usage:
        ./markdown2html.py [input_file] [output_file]

    Arguments:
        input_file: path to the Markdown file
	output_file: path to the output HTML file

    Example:
        ./markdown2html.py README.md README.html
"""
if __name__ == "__main__":
    import sys
    from os import path
    import re

# Checking arguments
if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Checking file existence
if not path.exists(input_file) or not str(input_file).endswith(".md"):
    sys.stderr.write("Missing " + input_file + "\n")
    exit(1)

# if all checks are passed
exit(0)
