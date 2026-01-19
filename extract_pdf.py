import PyPDF2

pdf_path = r"c:\Users\BEZAKA\Desktop\Projet\New-Docs\IoT-MAB-master\docs\Algo.pdf"

try:
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        print(f"=== Extraction du PDF: {pdf_path} ===\n")
        print(f"Nombre de pages: {len(pdf_reader.pages)}\n")
        
        for i, page in enumerate(pdf_reader.pages):
            print(f"\n{'='*60}")
            print(f"PAGE {i+1}")
            print(f"{'='*60}\n")
            text = page.extract_text()
            if text:
                print(text)
            else:
                print("[Aucun texte détecté sur cette page]")
        
except Exception as e:
    print(f"Erreur: {e}")
    import traceback
    traceback.print_exc()
