Logistics Software

### **Description:**

Logistics software designed and intended for use in international air freight. This software should be fully able to create/edit all documentation required for standard air freight use. Documentation is but not limited to air waybills, and certificates of origin. As the project progresses, more features may come available.

# Basic Transaction Database
![Basic Transaction Database](https://d2mxuefqeaa7sj.cloudfront.net/s_57993C64AAC0E619FB55D1C5B2B95D9F764195EA077E5FD3D769702BB15776DC_1463511347407_file.png)


**Required Fields:** Reference, Client, Shipper, Consignee, Date  
  
Reference - Var Char  
Client - Char  
Shipper - Char  
Consignee - Char  
Date - Datetime  
  
## Adding a Transaction
![Adding a Transaction 1/2](https://d2mxuefqeaa7sj.cloudfront.net/s_57993C64AAC0E619FB55D1C5B2B95D9F764195EA077E5FD3D769702BB15776DC_1463511484035_file.png)

![Adding a Transaction 2/2](https://d2mxuefqeaa7sj.cloudfront.net/s_57993C64AAC0E619FB55D1C5B2B95D9F764195EA077E5FD3D769702BB15776DC_1463511564818_file.png)


**Required Fields:** Client, Shipper, Consignee, Point of Origin, Airport of Loading, Airport of Discharge, Ultimate Destination, Reference number, Consolidation No, Forwarder, Carrier  
  
Client - Char  
Shipper - Char  
Consignee - Char  
Point of Origin - Char  
Airport of Loading - Char   
Port of Discharge - Char  
Ultimate Destination - Char  
Reference Number - VarChar  
Consolidation No - VarChar  
Forwarder - Char  
Carrier - Char  
  
## Adding Documentation to Transaction
![Adding Docs](https://d2mxuefqeaa7sj.cloudfront.net/s_57993C64AAC0E619FB55D1C5B2B95D9F764195EA077E5FD3D769702BB15776DC_1463511665761_file.png)  
**Requirements:** AWB, Certificate of Origin  
**Description:** Must be able to add an Air Waybill, and Certificate of Origin.  
  
## **Adding an Air Waybill - Form
![awb #1](https://d2mxuefqeaa7sj.cloudfront.net/s_57993C64AAC0E619FB55D1C5B2B95D9F764195EA077E5FD3D769702BB15776DC_1463511784947_file.png)
**![awb #2](https://d2mxuefqeaa7sj.cloudfront.net/s_57993C64AAC0E619FB55D1C5B2B95D9F764195EA077E5FD3D769702BB15776DC_1463511886884_file.png)
**![awb #3](https://d2mxuefqeaa7sj.cloudfront.net/s_57993C64AAC0E619FB55D1C5B2B95D9F764195EA077E5FD3D769702BB15776DC_1463511902310_file.png)
**![awb #4](https://d2mxuefqeaa7sj.cloudfront.net/s_57993C64AAC0E619FB55D1C5B2B95D9F764195EA077E5FD3D769702BB15776DC_1463511951316_file.png)
**Requirements:** All fields present, Laser AWB (Print), 12 Inch AWB (Print)
**Not Required:** Checkboxes at bottom, Other printing options, Sales Reporting

----------
# Ideas
## Transaction Database
![Transaction DB](https://d2mxuefqeaa7sj.cloudfront.net/s_57993C64AAC0E619FB55D1C5B2B95D9F764195EA077E5FD3D769702BB15776DC_1463512831264_9F123BB6-E9E0-4070-A654-32B28B68A142-1-2048x1536-oriented.png)
**Database view example**

Reference  
Client  
Shipper  
Consignee  
A-1001–16  
SMP  
Jelec  
SMP France  

This is the basic transaction view of the Database. Only this info is required for the user to determine what shipment they want to view in more detail.  

----------
## Shipment view example  

**Shipment Information**

Client’s Name (Pulled from DB)  
Societe de maintenance petroliere  
45200 Chateau-Renard, France  
  
Airline Name   
Air France  
  
Shipper Name Here (Pulled from DB)  
Jelec USA  
16901 Park Row  
Houston, TX 77084  
  
Forwarder Name
Gail Winds Logistics
2700 Greens Rd STE H-200
Houston, TX 77032  
  
Agent (Should Default to Forwarder)  
Gail Winds Logistics  
2700 Greens Rd STE H-200  
Houston, TX 77032  
  
Handling Information  
Security Code XXXXXXXX  
Freight Prepaid  
Daniel Milholland PH: 281–449–8833  

### **Flight Information**
To (1)  
First Flight  
Via (2)  
Carrier (1)  
Via (2)  
Carrier (2)  
CDG  
AF/639/16Th  
N/A  
N/A  
N/A  
N/A  
  
**Cargo Information**
  
Handling Information  
ETA CDG: 08:50/18TH  
PO# 101–16–05–001  
INV# 16P001.01-CM001  
Nature of Goods  
Oilwell supplies  
AES ITN: XXXXXXXXXXXXXXXXXXXXXX  
  
**Pieces**

Pieces  
Weight  
Chargeable Weight  
Unit Price  
Total  
1  
50  
100  
1.75  
(Chargeable * Unit Price)  
  
**Additional Fees**  
  
Fuel  
123.00  
Security  
18.00  
Screening  
15.00  
EU Fee  
20.00  
  
### **Insurance Information (Optional)**  
Declared Value Freight  
Declared Value Customs  
Amount of Insurance  
NVD (NO VALUE DECLARED)  
NVD (NO VALUE DECLARED)  
NVD (NO VALUE DECLARED)  
  
### **Agent Information**  
Shipper or Agent  
Issuing Carrier or Agent  
Daniel Milholland / As Agent  
Daniel Milholland / As Agent  



