import os
import mysql.connector
import urllib.parse as urlparse


DATABASE_URL = os.getenv('mysql://uep6l1uhu56nkbi3:CNacQRq1VtTrNx01CoX6@btz7zr3tt1erxfbygo4e-mysql.services.clever-cloud.com:3306/btz7zr3tt1erxfbygo4e')

if not DATABASE_URL: raise ValueError("La variable d'environnement MYSQL_ADDON_URI est introuvable")

url = urlparse.urlparse(DATABASE_URL)

database = mysql.connector.connect(
    host='btz7zr3tt1erxfbygo4e-mysql.services.clever-cloud.com',
    user='uep6l1uhu56nkbi3',
    password='CNacQRq1VtTrNx01CoX6',
    database='btz7zr3tt1erxfbygo4e',
    port='3306'
)
