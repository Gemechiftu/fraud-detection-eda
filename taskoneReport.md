from pathlib import Path
from fpdf import FPDF

# Create the PDF content
report_title = "Interim Report – Task 1: Fraud Detection Project"
author = "Gemechiftu Diriba"
date = "July 20, 2025"

report_body = f"""
{report_title}
By {author}
Date: {date}

1. Dataset Summary
We worked with two datasets:
- Fraud_Data.csv: Contains transaction details, user information, and whether the transaction is fraud.
- IpAddress_to_Country.csv: Maps IP address ranges to country names.

2. Data Cleaning & Preprocessing
Performed the following:
- Removed duplicates
- Converted signup_time and purchase_time to datetime
- Handled missing values (if any)
- Merged IP information:
  - Converted IPs to integers
  - Merged using IP range matching

3. Feature Engineering
- time_since_signup: Seconds between signup and purchase
  Example: df['time_since_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()
- hour_of_day: Hour when purchase happened
- day_of_week: Day of the week
- ip_to_country: Mapped using IP range in IpAddress_to_Country.csv

4. Exploratory Data Analysis (EDA)
- Fraud distribution: Very imbalanced (e.g., 3% fraud, 97% non-fraud)
- Time-based insights: Fraud more likely during certain hours
- Device distribution: Mobile vs Desktop
- Browser usage: Certain browsers more fraud-prone
- IP country analysis: Top countries with fraud reports

Sample Visualizations:
- Pie chart of fraud vs. non-fraud
- Histograms: time_since_signup, hour_of_day
- Bar plots for browsers/devices/countries

5. Insights
- Most fraud occurs shortly after signup
- Some browsers/devices show more fraud
- IP address mapping helps identify country-based fraud hotspots

6. GitHub Repository
[🔗 Your Repo Link Here]
"""

# Create PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, report_title, ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=11)

for line in report_body.strip().split('\n'):
    pdf.multi_cell(0, 10, line.strip())

# Save PDF
output_path = "/mnt/data/Interim_Report_Task1_FraudDetection.pdf"
pdf.output(output_path)

output_path
