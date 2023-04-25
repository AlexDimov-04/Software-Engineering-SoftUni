def make_bold(func_ref):
    def wrapper(*args):
        return f'<b>{func_ref(*args)}</b>'

    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        return f'<i>{func_ref(*args)}</i>'

    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        return f'<u>{func_ref(*args)}</u>'

    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
