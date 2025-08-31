from flask import Flask, request, jsonify, render_template_string
import random, os

app = Flask(__name__)

# Load words from next.txt if available
if os.path.exists("next.txt"):
    with open("next.txt", "r") as f:
        words = f.read().split()
else:
    words = []

random.shuffle(words)

# HTML + CSS + JS combined
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LanguageBox</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }

    /* Button styles */
    .id {
      display: flex; align-items:center; justify-content: center;
      width: 200px; height: 50px;
      border-radius: 30px;
      border: 1px solid #8F9092;
      background-image: linear-gradient(to top, #D8D9DB 0%, #fff 80%, #FDFDFD 100%);
      font-size: 14px; font-weight: 600; color: #606060;
      cursor: pointer; transition: all 0.2s ease;
    }
    .id:hover {
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    /* Radio inputs */
    .radio-inputs {
      display: flex; justify-content: center;
      gap: 10px; margin-bottom: 20px;
    }
    .radio input { display: none; }
    .radio .name {
      padding: 10px 20px; border-radius: 10px;
      background: #eee; cursor: pointer;
      transition: all 0.3s ease;
    }
    .radio input:checked + .name {
      background: #2563eb; color: white;
      font-weight: bold;
    }

    #wordDisplay {
      margin-top: 30px; font-size: 28px;
      font-weight: bold; color: darkblue;
    }
  </style>
</head>
<body>
  <h1>LanguageBox</h1>

  <!-- Radio Buttons -->
  <div class="radio-inputs">
    <label class="radio">
      <input type="radio" name="length" value="3" checked>
      <span class="name">list 3</span>
    </label>
    <label class="radio">
      <input type="radio" name="length" value="4">
      <span class="name">list 4</span>
    </label>
    <label class="radio">
      <input type="radio" name="length" value="5">
      <span class="name">list 5</span>
    </label>
  </div>

  <!-- Next Button -->
  <button class="id" onclick="getNext()">Next</button>

  <!-- Word Display -->
  <div id="wordDisplay">Choose a word length and click Next!</div>

  <script>
    function getNext() {
      let length = document.querySelector('input[name="length"]:checked').value;
      fetch("/get_word", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: "length=" + length
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById("wordDisplay").innerText = data.word || data.message;
      });
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_code)

@app.route("/get_word", methods=["POST"])
def get_word():
    length = int(request.form.get("length", 0))
    filtered = [w for w in words if len(w) == length]
    if filtered:
        return jsonify({"word": random.choice(filtered)})
    else:
        return jsonify({"message": f"No {length}-letter words found. Please upload them to next.txt."})

if __name__ == "__main__":
    app.run(debug=True)
