#!/usr/bin/python3
"""
	This script is used to convert markdown to html. It takes 2 arguments.
	1. markdown file
	2. html file
"""
if __name__ == "__main__":
    import sys
    from os import path

# Checking arguments
if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    exit(1)

# Checking file existence
if not path.exists(sys.argv[1]) or not str(sys.argv[1]).endswith(".md"):
    sys.stderr.write("Missing " + sys.argv[1] + "\n")
    exit(1)

# if all checks are passed
exit(0)
