from openpyxl import load_workbook

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
    
    # Key values
    # Reference
    # AWB
    # Client
    # Shipper
    # Consignee
    # Airline
    # Forwarder
    # Ultimate Destination
    # To
    # Flight
    # Via-1
    # Carrier-1
    # Via-2
    # Carrier-2
    # Accounting
    # Handling
    # Pieces
    # Weight
    # Chargeable
    # Unit Price
    # L
    # W
    # H
    # Additional
    # Ammount
    # Agent
    # Customs
    # Freight
    # Insurance
    # Date
main()
    