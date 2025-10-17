import mysql.connector
from mysql.connector import Error
import logging
logging.basicConfig(level=logging.INFO)


try:
  
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chika12mark??",
    port=33306
  )

  if mydb.is_connected():
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    logging.info(" Database 'alx_book_store' created successfully!")
  cursor.close()
  mydb.close()
except Error as e:
  logging.info("Connection failed")

