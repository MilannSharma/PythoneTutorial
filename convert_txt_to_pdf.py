import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

styles = getSampleStyleSheet()
title_style = styles['Title']
heading_style = styles['Heading2']
normal_style = styles['Normal']

# Folders
folders = ['Basic Python', 'Advanced Python']

for folder in folders:
    if os.path.exists(folder):
        files = [f for f in os.listdir(folder) if f.endswith('.txt')]
        files.sort()
        for file in files:
            filepath = os.path.join(folder, file)
            pdf_filename = file.replace('.txt', '.pdf')
            pdf_path = os.path.join(folder, pdf_filename)
            doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            story = []
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            # Split content into lines
            lines = content.split('\n')
            for line in lines:
                if line.startswith('Chapter'):
                    story.append(Paragraph(line, heading_style))
                elif line.startswith('Theory:'):
                    story.append(Paragraph(line, normal_style))
                elif line.startswith('Code Example:'):
                    story.append(Paragraph(line, normal_style))
                else:
                    if line.strip():
                        # Add as code style
                        code_style = ParagraphStyle('code', parent=styles['Normal'], fontName='Courier', fontSize=8, leftIndent=20)
                        story.append(Paragraph(line, code_style))
            doc.build(story)
            print(f"PDF generated: {pdf_path}")

print("All individual PDFs generated.")
