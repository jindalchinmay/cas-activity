import os.path as op
path = op.dirname(op.realpath(__file__))
print(path)
path = op.join(op.dirname(op.realpath(__file__)), "reflection.pdf")
print(path)