from datetime import datetime

now : datetime = datetime.now()


date_var : str = f"{now:%Y-%m-%d}"
print(f"{now:%d-%m-%Y}")
print(date_var)

print(f"{now:%c}")