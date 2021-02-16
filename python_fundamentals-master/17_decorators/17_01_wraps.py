'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''
def html_wrap(text):
    def inner_func():
        print(f"html<p> {text}")
    return inner_func


text = "hello, Hi, nice to see you"
htmlwrapper = html_wrap(text)
htmlwrapper()
