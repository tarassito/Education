def grep(pattern):
   while True:
       line = yield
       if pattern in line:
           print(line)

g = grep("python")

next(g)
g.send('pty')
# >>>
g.send('python is')
# >>>python is
