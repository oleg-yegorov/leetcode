import sys, inspect


def get_module_classes(module_name, exclude_classes=None):
    classes = [obj for name, obj in inspect.getmembers(sys.modules[module_name]) if inspect.isclass(obj)]

    if exclude_classes:
        for exclude_class in exclude_classes:
            classes.remove(exclude_class)

    return classes
