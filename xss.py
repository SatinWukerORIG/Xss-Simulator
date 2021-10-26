import markdown
from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = 'secret key'

def render_md(filename=""):
    with open(filename) as md_file:
        return markdown.markdown(md_file.read())


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_md("index.md")

    session['content'] = request.form['text_content']
    return redirect("/show")

@app.route("/show")
def show():
    return f'<h1>Text you put:</h1>\n{session["content"]}'


if __name__ == '__main__':
    app.run(port=9999)