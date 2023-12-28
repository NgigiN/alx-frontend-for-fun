#!/usr/bin/python3
"""
	Checking arguments and file existence
"""
if __name__ == "__main__":
    import sys
    from os import path

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    exit(1)

if not path.exists(sys.argv[1]) or not str(sys.argv[1]).endswith(".md"):
    sys.stderr.write("Missing " + sys.argv[1] + "\n")
    exit(1)

exit(0)
