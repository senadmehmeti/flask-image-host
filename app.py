from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return "ok"

@app.route("/image")
def image():
    png = (
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01'
        b'\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\xf8\x0f'
        b'\x00\x01\x01\x01\x00\x18\xdd\x03\xdb\x00\x00\x00\x00IEND\xaeB`\x82'
    )

    resp = make_response(png)
    resp.headers["Content-Type"] = "image/png"
    resp.headers["Link"] = (
        'https://flask-image-host.onrender.com/log; rel="preload"; as="image"; '
        'referrerpolicy="unsafe-url"'
    )
    return resp

@app.route("/log")
def log():
    ref = request.headers.get("Referer", "NO REFERER")
    print("Referer:", ref)
    return f"Referer: {ref}\n", 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
