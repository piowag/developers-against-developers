import os

assert os.path.isfile(os.path.expanduser('~/task_two'))

with open(os.path.expanduser('~/task_two'), 'r') as f:
    assert f.read().strip() == "5"