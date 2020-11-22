import os

BASE_PATH = ""

def get_hierarchy(path):
    def get_contents(path, include_files=True):
        h = []
        p = {}
        files = os.listdir(path)
        for filename in os.listdir(path):
            try:
                contents = get_contents(f"{path}/{filename}")
                p[filename] = contents
            except:
                if include_files:
                    h.append(filename)
        if len(p):
            h.append(p)
        return h
    hierarchy = get_contents(path)
    return hierarchy

def get_contents(path):
    cont = os.listdir(path)
    cont = [i for i in cont if "__" not in i]
    cont = [i for i in cont if "." not in i] + sorted([i for i in cont if "." in i])
    return cont


def ulify(elements):
    string = "<ul>\n"
    string += "\n".join(["<li>" + str(s) + "</li>" for s in elements])
    string += "\n</ul>"
    return string

def make_url(base_url, element):
    return f"<a href={base_url.rstrip('/')}/{element}>{element}</a>"
