from pms5003 import PMS5003
import mariadb
import time
from datetime import datetime
datetime = datetime.now()
now = datetime.strftime("%H:%M:%S")
conn_params = {
	"user":"admin",
	"password":"password",
	"host":"localhost",
	"database":"mydatabase"
}
connection = mariadb.connect(**conn_params)
cursor=connection.cursor()
#cursor.execute("INSERT INTO")

print(
    """specific.py - Continuously submit a specific data value.

Press Ctrl+C to exit!

"""
)

# Configure the PMS5003 for Enviro+
# pins and ports may vary for your hardware!

# Default, assume Raspberry Pi compatible, running Raspberry Pi OS Bookworm
pms5003 = PMS5003(device="/dev/ttyAMA0", baudrate=9600)

insert=("INSERT INTO main_pmsreadings (time, pm10, pm25, pm100) VALUES (%s, %s, %s, %s)")

try:
    while True:
        data = (now ,pms5003.read().data[0],pms5003.read().data[1],pms5003.read().data[2])
        try:
            cursor.execute(insert, data)
            connection.commit()
            # cursor.execute("INSERT INTO pmsReadings (pm25, pm100) VALUES ", (pm25, pm100))
            print("Submitted!")
        except mariadb.Error as e:
            print(f"Error: {e}")
        
        time.sleep(2)

        #print("PM2.5 ug/m3 (combustion particles, metals, organic compounds)", pms5003.read().data[5], "\n", "PM10 ug/m3 (dust,pollen,mould)", pms5003.read().data[5])
        
        #data = pms5003.read()
        #print(f"PM2.5 ug/m3 (combustion particles, organic compounds, metals): {data.pm_ug_per_m3(2.5)}")
        #print(f"PM10 ug/m3 (dust, pollen, mould spores): {data.pm_ug_per_m3()}")

except KeyboardInterrupt:
    pass
    connection.close()
