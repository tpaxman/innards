import re
from typing import Optional
import inspect
import pandas as pd


def search_docstring(
        obj,
        lookup: str = None,
        casesensitive: bool = False,
        after: Optional[int] = None,
        before: Optional[int] = None,
        context: Optional[int] = None,
        *args,
        **kwargs
) -> None:
    """
    Searches within a docstring of an object
    """
    assert hasattr(obj, '__doc__'), 'object has no docstring'

    all_lines = obj.__doc__.split('\n')
    if lookup:
        if casesensitive:
            relevant_lines = [x for x in all_lines if lookup in x]
        else:
            relevant_lines = [x for x in all_lines if lookup.lower() in x.lower()]
    else:
        relevant_lines = all_lines
    print(*relevant_lines, sep='\n')


def print_signature(obj):
    """
    print the function signature
    """
    sig = inspect.signature(obj)
    print(f'return value = {sig.return_annotation}')

    d = {}
    for x in sig.parameters.values():
        bustup = re.split(r'\s*[:|=]\s*', str(x))
        name = bustup[0]
        if len(bustup) == 1:
            type_ = ''
            default = ''
        elif len(bustup) == 2:
            type_ = bustup[1]
            default = ''
        elif len(bustup) == 3:
            type_ = bustup[1]
            default = bustup[2]

        descrip = x.kind.description
        d[name] = {'type': type_, 'default': default, 'arg-category': descrip}

    df = pd.DataFrame(d)
    print(df.T.rename_axis('arg-name').to_markdown())


def describe_empty(obj):
    if obj == inspect._empty:
        return '<empty>'
    elif obj == None:
        return 'None'
    else:
        return obj
