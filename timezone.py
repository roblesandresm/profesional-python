from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print(f'Bogota: {bogota_date.strftime("%d/%m/%Y, %H:%M:%S")}')