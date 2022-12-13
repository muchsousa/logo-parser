# MIT No Attribution
#
# Copyright 2022 Rafael Guterres Jeffman
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THESOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

"""Create a syntax tree."""


def new_node(name):
    """Create a new node object."""
    return dict(name=name, children=[])


def append_node(node, new_node):
    """Append a node or leaf to a node."""
    assert isinstance(node, dict) and "children" in node
    node["children"].append(new_node)


def new_leaf(name, **kwargs):
    """Create a new leaf object."""
    return dict(name=name, value=kwargs)
