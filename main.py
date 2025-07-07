from fpdf import FPDF
import pandas as pd
import os

# Check if CSV file exists
if not os.path.exists("topics.csv"):
    print("Error: topics.csv file not found!")
    exit()

# Read CSV file
try:
    df = pd.read_csv("topics.csv")
    print(f"Found {len(df)} topics to process")
except Exception as e:
    print(f"Error reading CSV: {e}")
    exit()

# Create PDF
pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.set_auto_page_break(auto=True, margin=15)

# Add title page
pdf.add_page()
pdf.set_font("Times", "B", 20)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 30, "Python Programming Topics", align="C", ln=1)
pdf.ln(10)

# Add table of contents
pdf.set_font("Times", "B", 16)
pdf.cell(0, 15, "Table of Contents", ln=1)
pdf.ln(5)

pdf.set_font("Times", "", 12)
for index, row in df.iterrows():
    pdf.cell(0, 8, f"{index + 1}. {row['Topic']} - {row['Pages']} pages", ln=1)

# Generate topic pages
for index, row in df.iterrows():
    topic_name = row["Topic"]
    num_of_pages = int(row["Pages"])
    
    for page_num in range(num_of_pages):
        pdf.add_page()
        
        # Topic header with better formatting
        pdf.set_font("Times", "B", 16)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 15, f"Topic: {topic_name}", ln=1)
        
        # Page number for multi-page topics
        if num_of_pages > 1:
            pdf.set_font("Times", "I", 10)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(0, 8, f"Page {page_num + 1} of {num_of_pages}", ln=1)
        
        # Add underline
        pdf.set_draw_color(100, 100, 100)
        pdf.line(10, pdf.get_y(), 287, pdf.get_y())
        pdf.ln(10)
        
        # Notes section
        pdf.set_font("Times", "", 12)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(0, 10, "Notes:", ln=1)
        pdf.ln(5)
        
        # Add lined paper for notes
        pdf.set_draw_color(220, 220, 220)
        current_y = pdf.get_y()
        
        # Draw 12 lines for note-taking
        for line_num in range(12):
            line_y = current_y + (line_num * 8)
            if line_y < 180:  # Stay within page margins
                pdf.line(15, line_y, 280, line_y)
        
        # Add page number at bottom
        pdf.set_y(-15)
        pdf.set_font("Arial", "I", 8)
        pdf.set_text_color(128, 128, 128)
        pdf.cell(0, 10, f"Page {pdf.page_no()}", align="C")

# Save PDF
try:
    pdf.output("Python_Topics_Study_Guide.pdf")
    print("PDF generated successfully: Python_Topics_Study_Guide.pdf")
except Exception as e:
    print(f"Error saving PDF: {e}")