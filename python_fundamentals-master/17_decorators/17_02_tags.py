'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''
def html_wrap(tag, text):
    def inner_func():
        print(f"html<{tag}> {text}")
    return inner_func


text = "hello, Hi, nice to see you"
tag = 'p'
htmlwrapper = html_wrap(tag , text)
htmlwrapper()
