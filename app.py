from flask import Flask, render_template

app = Flask(__name__)

PDFS = {
    "graphics": {
        "title": "Graphics Portfolio",
        "file": "pdfs/Graphics_Portfolio.pdf",
    },
    "product": {
        "title": "Product Portfolio",
        "file": "pdfs/Product_Portfolio.pdf",
    },
    "cv": {
        "title": "CV",
        "file": "pdfs/CV.pdf",
    },
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/design/graphics")
def graphics_portfolio():
    return render_template("pdf_viewer.html", pdf=PDFS["graphics"])

@app.route("/design/product")
def product_portfolio():
    return render_template("pdf_viewer.html", pdf=PDFS["product"])

@app.route("/cv")
def cv():
    return render_template("pdf_viewer.html", pdf=PDFS["cv"])

@app.route("/code")
def code():
    return render_template("code.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/tictactoe")
def tictactoe():
    return render_template("code/tictactoe.html")

@app.route("/borderless")
def borderless():
    return render_template("code/borderless.html")

if __name__ == "__main__":
    app.run(debug=True)