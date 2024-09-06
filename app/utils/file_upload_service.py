import os 

class FileUploadService:
    def __init__(self,upload_folder) -> None:
        self.upload_folder = upload_folder

    def save_file(self, file, filename):
        if file:
            file_path = os.path.join(self.upload_folder,filename)
            file.save(file_path)
            return file_path
        
        return None
    
    def upload_translated_file(self,filename,translated_file):
        translated_filename = filename.replace(".pdf", "_translated.pdf")
        translated_path = self.save_file(translated_file, translated_filename)
        return translated_path
    
    
    def upload_slp(self,slp, translated_file):
        if slp:
            slp_filename = "Original_SLP.pdf"
            slp_path = self.save_file(slp, slp_filename)

            if translated_file:
                translated_path = self.upload_translated_file(slp_filename,translated_file)
                return slp_path, translated_path
            else:
                return slp_path,None
        else:
            return None,None
        
        
    def upload_list_of_dates(self,lod, translated_file):
        if lod:
            lod_filename = "List_of_Dates.pdf"
            lod_path = self.save_file(lod,lod_filename)

            if translated_file:
                translated_path = self.upload_translated_file(lod_filename,translated_file)
                return lod_path, translated_path
            else:
                return lod_path, None
        else:
            return None,None
    
    def upload_affidavit(self, affidavit, translated_file):
        if affidavit:
            affidavit_filename = "Affidavit.pdf"
            affidavit_path = self.save_file(affidavit, affidavit_filename)

            if translated_file:
                translated_path = self.upload_translated_file(affidavit_filename, translated_file)
                return affidavit_path, translated_path
            else:
                return affidavit_path, None
        else:
            return None,None

    def upload_vakalatnama(self, vakalatnama, translated_file):
        if vakalatnama:
            vakalatnama_filename = "Vakalatnama.pdf"
            vakalatnama_path = self.save_file(vakalatnama, vakalatnama_filename)

            if translated_file:
                translated_path = self.upload_translated_file(vakalatnama_filename, translated_file)
                return vakalatnama_path, translated_path
            else:
                return vakalatnama_path, None
        else:
            return None,None


    def upload_power_of_attorney(self, power_of_attorney, translated_file):
        if power_of_attorney:
            power_of_attorney_filename = "Power_of_Attorney.pdf"
            power_of_attorney_path = self.save_file(power_of_attorney, power_of_attorney_filename)

            if translated_file:
                translated_path = self.upload_translated_file(power_of_attorney_filename, translated_file)
                return power_of_attorney_path, translated_path
            else:
                return power_of_attorney_path, None
        else:
            return None,None


    def upload_certificate_advocate(self, certificate_advocate, translated_file):
        if certificate_advocate:
            certificate_advocate_filename = "Certificate_Advocate.pdf"
            certificate_advocate_path = self.save_file(certificate_advocate, certificate_advocate_filename)

            if translated_file:
                translated_path = self.upload_translated_file(certificate_advocate_filename, translated_file)
                return certificate_advocate_path, translated_path
            else:
                return certificate_advocate_path, None
        else:
            return None,None

    def upload_memo_of_appearance(self, memo_of_appearance, translated_file):
        if memo_of_appearance:
            memo_of_appearance_filename = "Memo_of_Appearance.pdf"
            memo_of_appearance_path = self.save_file(memo_of_appearance, memo_of_appearance_filename)

            if translated_file:
                translated_path = self.upload_translated_file(memo_of_appearance_filename, translated_file)
                return memo_of_appearance_path, translated_path
            else:
                return memo_of_appearance_path, None
        else:
            return None,None


    def upload_oath_of_translator(self, oath_of_translator, translated_file):
        if oath_of_translator:
            oath_of_translator_filename = "Oath_of_Translator.pdf"
            oath_of_translator_path = self.save_file(oath_of_translator, oath_of_translator_filename)

            if translated_file:
                translated_path = self.upload_translated_file(oath_of_translator_filename, translated_file)
                return oath_of_translator_path, translated_path
            else:
                return oath_of_translator_path, None
        else:
            return None,None

    
    def upload_annexures(self, annexures, annexures_translated):
        annexure_paths = []
        annexure_translated_paths = []
        
        if annexures:
            for count, annexure in enumerate(annexures):
                # Save the annexure file
                annexure_filename = f"Annexure_{count}.pdf"
                annexure_path = self.save_file(annexure, annexure_filename)
                annexure_paths.append(annexure_path)

                # Check if there's a corresponding translation
                if annexures_translated and len(annexures_translated) > count and annexures_translated[count]:
                    annexure_translated_filename = annexure_filename.replace(".pdf", "_translated.pdf")
                    annexure_translated_path = self.save_file(annexures_translated[count], annexure_translated_filename)
                    annexure_translated_paths.append(annexure_translated_path)
                else:
                    # Handle the case where a translation is missing
                    annexure_translated_paths.append(None)  # Append None to maintain alignment of indexes
                    print(f"Warning: No translation uploaded for {annexure_filename}")

            return annexure_paths, annexure_translated_paths
        else:
            return None,None

    



    

    



        
    
    
    
        
    