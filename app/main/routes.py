from flask import Blueprint, request, render_template, current_app
from ..utils.file_upload_service import FileUploadService

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/upload", methods=["POST"])
def upload_files():
    file_service = FileUploadService(current_app.config['UPLOAD_FOLDER'])
    
    # Retrieve files from the request
    slp = request.files.get("slp")
    slp_translated = request.files.get("slp_translated")
    list_of_dates = request.files.get("list_of_dates")
    list_of_dates_translated = request.files.get("list_of_dates_translated")
    affidavit = request.files.get("affidavit")
    affidavit_translated = request.files.get("affidavit_translated")
    vakalatnama = request.files.get("vakalatnama")
    vakalatnama_translated = request.files.get("vakalatnama_translated")
    power_of_attorney = request.files.get("power_of_attorney")
    certificate_by_advocate = request.files.get("certificate_by_advocate")
    memo_of_appearance = request.files.get("memo_of_appearance")
    memo_of_appearance_translated = request.files.get("memo_translated")
    annexures = request.files.getlist("annexures[]")
    annexures_translated = request.files.getlist("annexures_translated[]")
    oath_of_translator = request.files.get("oath_of_translator")


    
    # Save SLP file and translation

    slp_path, slp_translated_path = file_service.upload_slp(slp, slp_translated)
    list_of_dates_path, list_of_dates_translated_path = file_service.upload_list_of_dates(list_of_dates,list_of_dates_translated)
    affidavit_path,affidavit_translated_path = file_service.upload_affidavit(affidavit,affidavit_translated)
    vakalatnama_path, vakalatnama_translated_path = file_service.upload_vakalatnama(vakalatnama,vakalatnama_translated)
    power_of_attorney_path, power_of_attorney_translated_path = file_service.upload_power_of_attorney(power_of_attorney,False) # False is provided because there is no translated file for power of attorney
    certificate_by_advocate_path, certificate_by_advocate_translated_path = file_service.upload_certificate_advocate(certificate_by_advocate,False)
    memo_of_appearance_path, memo_of_appearance_translated = file_service.upload_memo_of_appearance(memo_of_appearance, memo_of_appearance_translated)
    oath_of_translator_path, oath_of_translator_translated = file_service.upload_oath_of_translator(oath_of_translator, False)


    # Save Annexure
    annexure_paths, annexure_translated_paths = file_service.upload_annexures(annexures, annexures_translated)
    
    # Add logic for further processing after file uploads (e.g., OCR, scrutiny)

    return "Files uploaded successfully"
