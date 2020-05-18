#!/usr/bin/env python
# coding=utf-8


import importlib

def import_function(module):
    """
    This function is to used to import a function/class string

    EXAMPLES:
    function1 = import_function("src.python.module1.function1")
    function1()

    :param module: string - the full function path to import , src.python.mymodule.myfunction
    :return: function
    """
    p, m = module.rsplit(".", 1)
    mod = importlib.import_module(p)
    return getattr(mod, m)













