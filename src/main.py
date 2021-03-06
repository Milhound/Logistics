from openpyxl import load_workbook
from PIL import Image, ImageFont, ImageDraw

try:
    template = Image.open('resources/blank_airwaybill.jpg')
    pdf = ImageDraw.Draw(template)
    awb_font = ImageFont.truetype('Arial', 65)
    font = ImageFont.truetype('Arial', 40)
    small_font = ImageFont.truetype('Arial', 32)
except:
    print("Could not locate AWB template")
    raise

# Load the test file
wb = load_workbook('example/Example.xlsx')
# Get worksheet
try:
    ws = wb['Data']
except:
    print("Could not find a Sheet in excel with the name Data.")
    raise

def get_row_data(row):
    row_array = []
    for cell in row:
        row_array.append(str(cell.value).strip())
    return row_array

def main():
    keys = get_row_data(ws.rows[0])
    values = get_row_data(ws.rows[1])
    data = dict(zip(keys, values))
    
    pdf.text((100, 125), data['AWB'][:3], (255,0,0), font=awb_font)
    pdf.text((380, 125), data['AWB'][4:], (255,0,0), font=awb_font)
    pdf.text((238, 125), data['Departing'], (0,0,0), font=awb_font)
    pdf.text((130,275), data['Shipper'], (0,0,0), font=font)
    pdf.text((1600, 255), data['Airline'], (0,0,0), font=font)
    pdf.text((130, 500), data['Consignee'], (0,0,0), font=font)
    pdf.text((130, 750), data['Forwarder'], (0,0,0), font=font)
    pdf.text((1350, 775), data['Accounting'], (0,0,0), font=font)
    pdf.text((800, 935), data['Departing'], (0,0,0), font=font)
    pdf.text((140, 1028), data['To'], (0,0,0), font=font)
    pdf.text((300, 1028), data['Flight'], (0,0,0), font=font)
    pdf.text((875, 1028), data['Via-1'], (0,0,0), font=font)
    pdf.text((990, 1028), data['Carrier-1'], (0,0,0), font=font)
    pdf.text((1100, 1028), data['Via-2'], (0,0,0), font=font)
    pdf.text((1225, 1028), data['Carrier-2'], (0,0,0), font=font)
    pdf.text((1335, 1028), 'USD', (0,0,0), font=font)
    pdf.text((1458, 1028), data['Terms'], (0,0,0), font=font)
    if (data['Terms'] == 'PP'):
        pdf.text((1532, 1042), 'X', (0,0,0), font=font)
        pdf.text((1665, 1042), 'X', (0,0,0), font=font)
    if (data['Terms'] == 'CC'):
        pdf.text((1597, 1042), 'X', (0,0,0), font=font)
        pdf.text((1732, 1042), 'X', (0,0,0), font=font)
    pdf.text((1870, 1028), data['Freight'], (0,0,0), font=font)
    pdf.text((2185, 1028), data['Customs'], (0,0,0), font=font)
    pdf.text((230, 1150), data['To'] + ', ' + data['Ultimate Destination'], (0,0,0), font=font)
    pdf.text((800, 1150), data['Flight-1'], (0,0,0), font=font)
    pdf.text((1100, 1150), data['Flight-2'], (0,0,0), font=font)
    pdf.text((1475, 1140), data['Insurance'], (0,0,0), font=font)
    pdf.text((175, 1245), data['Handling'], (0,0,0), font=small_font)
    pdf.text((175, 1280), data['Handling-2'], (0,0,0), font=small_font)
    pdf.text((175, 1317), data['Handling-3'], (0,0,0), font=small_font)
    pdf.text((170, 1470), data['Pieces'], (0,0,0), font=font)
    pdf.text((320, 1470), data['Weight'], (0,0,0), font=font)
    pdf.text((925, 1470), data['Chargeable'], (0,0,0), font=font)
    pdf.text((1200, 1470), data['Unit Price'], (0,0,0), font=font)
    pdf.text((1580, 1470), str(float(data['Chargeable']) + float(data['Unit Price'])), (0,0,0), font=font)
    pdf.text((1900, 1470), data['Nature'], (0,0,0), font=small_font)
    if (data['Nature-2'] != 'None'):
        pdf.text((1900, 1510), data['Nature-2'], (0,0,0), font=small_font)
    if (data['Nature-3'] != 'None'):
        pdf.text((1900, 1560), data['Nature-3'], (0,0,0), font=small_font)
    if (data['Nature-4'] != 'None'):
        pdf.text((1900, 1600), data['Nature-4'], (0,0,0), font=small_font)
    if (data['Nature-5'] != 'None'):
        pdf.text((1900, 1640), data['Nature-5'], (0,0,0), font=small_font)
    pdf.text((1580, 2120), str(float(data['Chargeable']) + float(data['Unit Price'])), (0,0,0), font=font)
    if (data['Additional'] == 'F'):
        pdf.text((1100, 2220), 'Fuel', (0,0,0), font=font)
    pdf.text((2000, 1900), 'Dimensions', (0,0,0), font=font)
    
    pdf.text((1430, 2700), data['Agent'] + ' / AS AGENT', (0,0,0), font=font)
    pdf.text((1720, 2900), data['Agent'] + ' / AS AGENT', (0,0,0), font=font)
    pdf.text((1720, 3010), data['AWB'], (255,0,0), font=awb_font)
    
    template.show()
main()
    