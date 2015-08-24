import xlrd
import MySQLdb

def print_xls():
  loc_of_file = "C:/Users/Hemant/Desktop/Daric/150714 iam pipeline - adjusted for Daric.com.xlsx"
  book = xlrd.open_workbook(loc_of_file)
  sheet = book.sheet_by_name("Sheet1")
  #SQL connection
  database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "mysqlPython")
  #Cursor to go through database
  cursor = database.cursor()
  # Create the INSERT INTO sql query
  query = """INSERT INTO stats_table (col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17) 
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
  #Loop to go through all the tables
  for r in range(1, sheet.nrows):
    col1 = sheet.cell(r,1).value
    col2 = sheet.cell(r,2).value
    col3 = sheet.cell(r,3).value
    col4 = sheet.cell(r,4).value
    col5 = sheet.cell(r,5).value
    col6 = sheet.cell(r,6).value
    col7 = sheet.cell(r,7).value
    col8 = sheet.cell(r,8).value
    col9 = sheet.cell(r,9).value
    col10 = sheet.cell(r,10).value
    col11 = sheet.cell(r,11).value
    col12 = sheet.cell(r,12).value
    col13 = sheet.cell(r,13).value
    col14 = sheet.cell(r,14).value
    col15 = sheet.cell(r,15).value
    col16 = sheet.cell(r,16).value
    col17 = sheet.cell(r,17).value
    values = (col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17)
    #Execute the SQL
    cursor.execute(query, values)
  #Close the cursor  
  cursor.close()
  #Commit transaction
  database.commit()
  #Close database connection
  database.close()

if __name__ == "__main__":
  print_xls()
