from openpyxl import load_workbook

# Load the test file
wb = load_workbook('../example/Example.xlsx')
# Get worksheet
try:
    ws = wb['Data']
    for row in ws.rows:
        for cell in row:
           print(cell.value)
        
except:
    print("Could not find a Sheet in excel with the name Data.")


