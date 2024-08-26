from flask import Blueprint,request,jsonify,render_template, redirect, url_for,current_app
import os
import fitz # PyMuPDF
from ..nlp.SLP_scrutinizer import SLP

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

    #document = request.files
    
    slp_obj = SLP(slp)
    

   
    


    return redirect(url_for("main.index"))


