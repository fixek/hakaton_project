import sqlite3wwwwdw

conn = sqlite3.connect("shedule.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Вставляем данные в таблицу
a = cursor.execute("SELECT Column2 FROM main.INF WHERE Column1 = ?", ("Понедельник",))
print(a.fetchall())