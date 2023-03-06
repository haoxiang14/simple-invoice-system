import jinja2
import pdfkit
from datetime import datetime

date = datetime.today().strftime('%d-%m-%Y')
invoice_number = input("Enter invoice number: ")
hours_1 = int(input("Enter hours worked for first week: "))
hours_2 = int(input("Enter hours worked for second week: "))
hours_3 = int(input("Enter hours worked for third week: "))
hours_4 = int(input("Enter hours worked for fourth week: "))
hours_5 = int(input("Enter hours worked for fifth week: "))

amount_1 = hours_1 * 15
amount_2 = hours_2 * 15
amount_3 = hours_3 * 15
amount_4 = hours_4 * 15
amount_5 = hours_5 * 15

total_amount = amount_1 + amount_2 + amount_3 + amount_4 + amount_5

context = {'date': date, 'invoice_number': invoice_number, 'hours_1': hours_1, 'hours_2': hours_2, 'hours_3': hours_3, 'hours_4': hours_4, 'hours_5': hours_5, 'amount_1': amount_1, 'amount_2': amount_2, 'amount_3': amount_3, 'amount_4': amount_4, 'amount_5': amount_5, 'total_amount': total_amount}

templateLoader = jinja2.FileSystemLoader("./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template('invoice.html')
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
pdfkit.from_string(output_text, 'invoice.pdf', configuration=config)

