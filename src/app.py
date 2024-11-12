from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Simple Form</title>
  </head>
  <body>
    <h1>Say something:</h1>
    <form method="POST">
      <input type="text" name="input_text" required>
      <button type="submit">Send</button>
    </form>
    {% if result %}
      <h2>You've said: {{ result }}... How smart you are! :-)</h2>
    {% endif %}
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        result = request.form['input_text']
    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
