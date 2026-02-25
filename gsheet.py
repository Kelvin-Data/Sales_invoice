import pygsheets
import dotenv
import os

dotenv.load_dotenv()

def get_gsheet_data():
  path = os.getenv("GSHEET_PATH")
  print(path)

  gc = pygsheets.authorize(service_account_file = path)
  print('gsheets connected')

  sh = gc.open('Invoice_form')
  wk = sh.worksheet_by_title('Form_responses')
  print("Gsheet opened")

  content = wk.get_all_values(include_tailing_empty=False)
  
  data_rows = content[1:]  

  for row in data_rows:
    # Only print non-empty rows
    if any(cell.strip() for cell in row):
      print(row)  
    
  return data_rows
