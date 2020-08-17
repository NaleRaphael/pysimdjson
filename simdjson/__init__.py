"""High-level bindings for the simdjson project."""
import json

try:
    from csimdjson import (
        # Objects
        Parser,
        Array,
        Object,
        # Constants
        MAXSIZE_BYTES,
        PADDING,
        DEFAULT_MAX_DEPTH
    )
except ImportError:
    raise RuntimeError('Unable to import low-level simdjson bindings.')

# Shuts up *all* linters complaining about our unused imports.
_ALL_IMPORTS = [
    Parser,
    Array,
    Object,
    MAXSIZE_BYTES,
    PADDING,
    DEFAULT_MAX_DEPTH
]


def load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None,
         parse_constant=None, object_pairs_hook=None, **kwargs):
    """
    Same as the built-in json.load(), with the following exceptions:

        - All parse_* arguments are currently ignored. simdjson does not
          currently provide hooks for these, but it is planned.
        - object_pairs_hook is ignored.
        - cls is ignored.
    """
    content = fp.read()
    if isinstance(content, str):
        content = content.encode('utf-8')

    parser = Parser()
    return parser.parse(content, True)


def load_lines(fp, *, cls=None, object_hook=None, parse_float=None,
               parse_int=None, parse_constant=None, object_pairs_hook=None,
               **kwargs):
    """
    A specialized method to load JSON lines document (.jsonl). Since a JSON
    lines document can be taken as a single file containing multiple JSON
    documents, we can utilize `simdjson.load_many()` to load and parse it in
    a lower level (C++) to avoid redundant object creations in Python side.

    However, this method is not fully functional just like the `load()` method
    above.
    """
    parser = Parser()
    return parser.load_lines(fp, recursive=True)


def loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None,
          parse_constant=None, object_pairs_hook=None, **kwargs):
    """
    Same as the built-in json.loads(), with the following exceptions:

        - All parse_* arguments are currently ignored. simdjson does not
          currently provide hooks for these, but it is planned.
        - object_pairs_hook is ignored.
        - cls is ignored.
    """
    if isinstance(s, str):
        s = s.encode('utf-8')

    parser = Parser()
    return parser.parse(s, True)


def loads_lines(s, *, cls=None, object_hook=None, parse_float=None,
                parse_int=None, parse_constant=None, object_pairs_hook=None,
                **kwargs):
    """
    Same as `load_lines()`, but it takes string as input.
    """
    parser = Parser()
    return parser.parse_lines(s, recursive=True)


dumps = json.dumps
dump = json.dump
