from flask import Blueprint, request, render_template, redirect, url_for, current_app
from ..nlp.SLP_scrutinizer import SLP
from ..nlp.Document_scrutinizer import Document
from ..nlp.Affidavit_scrutinizer import Affidavit
from ..nlp.Vakalatnama_scrutinizer import Vakalatnama
from ..nlp.Memo_app_scrutinizer import Memo_of_appearance
from ..nlp.Annexure_scrutinizer import Annexure
import os

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/upload", methods=["POST"])
def upload_files():
    global slp_object
    
    slp = request.files.get("slp")
    translated_file = request.files.get("slp_translated")
    translator_oath = request.files.get("translator_oath")
    list_of_dates = request.files.get("list_of_dates")
    list_of_dates_translated = request.files.get("list_of_dates_translated")
    affidavit = request.files.get("affidavit")
    affidavit_translated = request.files.get("affidavit_translated")
    vakalatnama = request.files.get("vakalatnama")
    vakalatnama_translated = request.files.get("vakalatnama_translated")
    power_of_attorney = request.files.get("power_of_attorney")
    certificate_by_advocate = request.files.get("certificate_by_advocate")
    memo_of_appearance = request.files.get("memo_of_appearance")
    memo_translated = request.files.get("memo_translated")
    power_of_attorney_memo = request.files.get("power_of_attorney_memo")
    annexures = request.files.getlist("annexures[]")
    annexures_translated = request.files.getlist("annexures_translated[]")
    oath_of_translator = request.files.get("oath_of_translator")
    language = request.form.get("language")

    upload_folder = current_app.config['UPLOAD_FOLDER']

    # Save the SLP file
    if slp:
        slp.filename = "Original SLP.pdf"
        slp.save(os.path.join(upload_folder, slp.filename))
        if translated_file:
            translated_filename = slp.filename.replace(".pdf","_translated.pdf")
            translated_file_path = os.path.join(upload_folder, translated_filename)
            translated_file.save(translated_file_path)
        

    # Save the List of Dates file and its translated version
    if list_of_dates:
        list_of_dates.filename = "List of dates.pdf"
        list_of_dates_path = os.path.join(upload_folder, list_of_dates.filename)
        list_of_dates.save(list_of_dates_path)
        
        if list_of_dates_translated:
            list_of_dates_translated_filename = list_of_dates.filename.replace('.pdf', '_translated.pdf')
            list_of_dates_translated_path = os.path.join(upload_folder, list_of_dates_translated_filename)
            list_of_dates_translated.save(list_of_dates_translated_path)
    
    # Save the Affidavit file and its translated version
    if affidavit:
        affidavit.filename = "Affidavit.pdf"
        affidavit_path = os.path.join(upload_folder, affidavit.filename)
        affidavit.save(affidavit_path)
        
        if affidavit_translated:
            affidavit_translated_filename = affidavit.filename.replace('.pdf', '_translated.pdf')
            affidavit_translated_path = os.path.join(upload_folder, affidavit_translated_filename)
            affidavit_translated.save(affidavit_translated_path)

    # Save the Vakalatnama file and its translated version
    if vakalatnama:
        vakalatnama.filename = "Vakalatnama.pdf"
        vakalatnama_path = os.path.join(upload_folder, vakalatnama.filename)
        vakalatnama.save(vakalatnama_path)
        
        # Save the translated version
        if vakalatnama_translated:
            vakalatnama_translated_filename = vakalatnama.filename.replace('.pdf', '_translated.pdf')
            vakalatnama_translated_path = os.path.join(upload_folder, vakalatnama_translated_filename)
            vakalatnama_translated.save(vakalatnama_translated_path)

        # Save the Power of Attorney file if provided
        if power_of_attorney:
            power_of_attorney.filename = "Power of Attorney.pdf"
            power_of_attorney_path = os.path.join(upload_folder, power_of_attorney.filename)
            power_of_attorney.save(power_of_attorney_path)

        # Save the Certificate by Advocate file if provided
        if certificate_by_advocate:
            certificate_by_advocate.filename = "Certificate by Advocate.pdf"
            certificate_by_advocate_path = os.path.join(upload_folder, certificate_by_advocate.filename)
            certificate_by_advocate.save(certificate_by_advocate_path)

    # Save the Memo of Appearance file and its translated version
    if memo_of_appearance:
        memo_of_appearance.filename = "Memo of Appearance"
        memo_of_appearance_path = os.path.join(upload_folder, memo_of_appearance.filename)
        memo_of_appearance.save(memo_of_appearance_path)
        
        if memo_translated:
            memo_translated_filename = memo_of_appearance.filename.replace('.pdf', '_translated.pdf')
            memo_translated_path = os.path.join(upload_folder, memo_translated_filename)
            memo_translated.save(memo_translated_path)

        # Save the Power of Attorney (Memo) file if provided
        if power_of_attorney_memo:
            power_of_attorney_memo.filename = "Power of Attorney (Memo)"
            power_of_attorney_memo_path = os.path.join(upload_folder, power_of_attorney_memo.filename)
            power_of_attorney_memo.save(power_of_attorney_memo_path)

    # Save each Annexure file and its translated versions
    if annexures:
        global annexure_objects
        annexure_objects = []
        for count, annexure in enumerate(annexures):
            annexure.filename = f"Annexure {count}.pdf"
            annexure_path = os.path.join(upload_folder, annexure.filename)
            annexure.save(annexure_path)

            # Create an Annexure object for each uploaded annexure
            annexure_obj = Annexure(annexure)
            annexure_objects.append(annexure_obj)

            if annexures_translated and len(annexures_translated) > count:
                annexure_translated = annexures_translated[count]
                annexure_translated_filename = annexure.filename.replace(f'.pdf',f'_translated.pdf')
                annexure_translated_path = os.path.join(upload_folder, annexure_translated_filename)
                annexure_translated.save(annexure_translated_path)
    
    # Save the Oath of Translator file
    if oath_of_translator:
        oath_of_translator.filename = 'Oath_of_translator.pdf'
        oath_of_translator_path = os.path.join(upload_folder, oath_of_translator.filename)
        oath_of_translator.save(oath_of_translator_path)

    # Process the files or redirect as needed
    if list_of_dates:
        global lod
        lod = Document(list_of_dates)
    if translated_file:
        if list_of_dates:
            slp_object = SLP(file=slp, lod=lod, translated_file_path=translated_file_path, list_of_dates_path=list_of_dates_path)
        else:
            slp_object = SLP(file=slp, translated_file_path=translated_file_path)
    elif list_of_dates:
        slp_object = SLP(file=slp,lod=lod, list_of_dates_path=list_of_dates_path)
    else:
        slp_object = SLP(file=slp)

    # Add affidavit processing if needed
    if affidavit:
        global affidavit_obj
        affidavit_obj = Affidavit(affidavit)
     
    if vakalatnama:
        global vakalatnama_obj 
        vakalatnama_obj = Vakalatnama(vakalatnama)
    
    if memo_of_appearance:
        global memo_of_appearance_obj 
        memo_of_appearance_obj  = Memo_of_appearance(memo_of_appearance)

    slp_object.slp_trigger()

    if "affidavit_obj" in globals():
        affidavit_obj.affidavit_trigger()
    if "vakalatnama_obj" in globals():
        vakalatnama_obj.vakalatnama_trigger()
    if "memo_of_appearance_obj" in globals():
        memo_of_appearance_obj.memo_trigger()

    if "annexure_objects" in globals():
        for annexure_obj in annexure_objects:
            annexure_obj.annexure_trigger()
            
    return redirect(url_for("main.show_defects"))

@main.route("/show_defects")
def show_defects():

    

    # Example defect dictionaries; these should be populated by your application's logic
    if "slp_object" in globals():
        slp_defects = slp_object.slp_defects

        defects_data = {
            "slp_defects": slp_defects
        }

    if 'lod' in globals():
        lod_defects = lod.common_defects
        defects_data["lod_defects"] = lod_defects
    
    if 'vakalatnama_obj' in globals():
        vakalatnama_defects = vakalatnama_obj.vakalatnama_defects
        defects_data["vakalatnama_defects"] = vakalatnama_defects
    
    if 'memo_of_appearance_obj' in globals():
        memo_of_appearance_defects = memo_of_appearance_obj.memo_of_appearance_defects
        defects_data["memo_of_appearance_defects"] = memo_of_appearance_defects
    
    if 'affidavit_obj' in globals():
        affidavit_defects = affidavit_obj.affidavit_defects
        defects_data["affidavit_defects"] = affidavit_defects
        txt=""
        for txt in affidavit_obj.text.values():
            txt+= txt
        print(txt)
    
    if 'annexure_objects' in globals():
        annexure_defects = [annexure.annexure_defects for annexure in annexure_objects]
        defects_data["annexure_defects"] = annexure_defects

    return render_template("defects.html", defects=defects_data)
