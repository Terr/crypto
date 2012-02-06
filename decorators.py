def uppercase_text(fun):
    def to_upper(self, text, *args, **kwargs):
        text = text.upper()
        return fun(self, text, *args, **kwargs)
    return to_upper

