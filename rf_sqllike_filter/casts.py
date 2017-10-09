# encoding: utf8

from .exceptions import BadValue

def make_simple_cast(cast_func, name):
    def cast(value, field):
        try:
            return cast_func(value.strip())
        except ValueError, e:
            raise BadValue("Can not parse {0} value \"{1}\" for field \"{2}\": {3}".format(
                        name,
                        value,
                        field.name,
                        e.message
            ))
    return cast

cast_int = make_simple_cast(int, 'integer')
cast_float = make_simple_cast(float, 'float')