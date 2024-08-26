from flask import Blueprint,request,jsonify,render_template, redirect, url_for,current_app
import os
import fitz # PyMuPDF

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/upload",methods=["POST"])
def upload_files():
    #Get the uploaded files from the form

    slp = request.files["slp"]
    file2 = request.files["file2"]
    file3 = request.files["file3"]

    # Save the files
    if slp:
        slp.save(os.path.join(current_app.config['UPLOAD_FOLDER'], slp.filename))
    if file2:
        file2.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file2.filename))
    if file3:
        file3.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file3.filename))

    

    # Load the pdf and extract the dimensions for each page

    slp_path = f"uploads/{slp.filename}"
    slp_doc = fitz.open(slp_path)
    slp_page_dimensions = [(page.rect.width, page.rect.height) for page in slp_doc]

    print(slp_page_dimensions)


    return redirect(url_for("main.index"))

