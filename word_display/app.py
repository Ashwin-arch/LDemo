from flask import Flask, render_template_string
import random
app = Flask(__name__)

# Read and split words once
with open("next.txt", "r") as f:
    words = f.read().split()
random.shuffle(words)
# HTML with button + JS
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Word Viewer</title>
</head>
<body>
    <h1>Word display</h1>
    <h2 id="word">Click Next to start</h2>
    <button onclick="nextWord()">Next</button>

    <script>
        let words = {{ words|tojson }};
        let index = 0;

        function nextWord() {
            if (index < words.length) {
                document.getElementById("word").innerText = words[index];
                index++;
            } else {
                document.getElementById("word").innerText = "No more words!";
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, words=words)

if __name__ == "__main__":
    app.run(debug=True)
