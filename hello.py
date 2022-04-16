#!/usr/bin/env python3

import pygit2
from pygit2 import Repository

repo = Repository('.git')
last = repo[repo.head.target]

print("""<html>
<body>
<p>Hello, Roland!<p/>""")

print("""
<p>Git log is:
<pre>""")

for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
	print(commit.message)

print("""
</pre>
</p>
""")

print("""
</body>
</html>""")
