from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import pandas as pd

# -----------------------------
# READ DATA FROM FILE
# -----------------------------
df = pd.read_csv("student_data.csv")

# -----------------------------
# DATA ANALYSIS
# -----------------------------
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

# -----------------------------
# PDF REPORT GENERATION
# -----------------------------
doc = SimpleDocTemplate("Student_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("<b>Student Performance Report</b>", styles["Title"]))
elements.append(Spacer(1, 12))

# Summary
elements.append(Paragraph(f"Average Marks: {average_marks}", styles["Normal"]))
elements.append(Paragraph(f"Highest Marks: {highest_marks}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Marks: {lowest_marks}", styles["Normal"]))
elements.append(Spacer(1, 12))

# Table
table_data = [df.columns.tolist()] + df.values.tolist()
table = Table(table_data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
]))

elements.append(table)

doc.build(elements)

print("PDF Report Generated Successfully")
