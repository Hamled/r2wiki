import os
import re
import sys
import pydoc

"""
Directions on how to setup is in the wiki itself
"""

try:
	src_dir = os.path.dirname(os.path.realpath(__file__))
	pattern = re.compile (sys.argv[1])

	found = ''

	for path, subdirs, files in os.walk(src_dir):
		for name in files:
			md_path = os.path.join(path, name)
			if not '.git' in md_path and md_path.endswith('.md'):
				with open(md_path, 'r') as f:
					for lines in f.readlines():
						if re.search(pattern, lines):
							if not any(filter in lines for filter in ['<p hidden>',
																	  '<!--',
																	  'LGPL3',
																	  'DCPU']):
								match = ((re.sub('\*\*', '', lines)).lstrip() + '\n').replace('`', "'")
								if match.startswith('- ['):
									found += 'https://radare2.securisec.com%s' % match.split(']')[-1].strip('(')
								else:
									found += match

	pydoc.pager(found)
except IndexError:
	print 'Usage: %s search_param' % sys.argv[0]

# TODO: add color highlight on matches