from typing import Optional
import inspect

def search_docstring(
        obj,
        lookup: str = None,
        casesensitive: bool = False,
        after: Optional[int] = None,
        before: Optional[int] = None,
        context: Optional[int] = None
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
    for x in inspect.signature(obj).parameters.values():
        print(x)
