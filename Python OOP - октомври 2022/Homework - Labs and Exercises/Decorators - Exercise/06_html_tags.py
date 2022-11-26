def tags(tag):
    def decorator(func_ref):
        def wrapper(*args):
            return f"<{tag}>{func_ref(*args)}</{tag}>"

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
