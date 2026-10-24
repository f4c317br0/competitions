from datetime import datetime, timedelta

s = input().strip()
date = datetime.strptime(s, "%d.%m.%Y")
y = date.year
if date.month <= 2:
    y -= 1
diff = y // 100 - y // 400 - 2
result = date - timedelta(days=diff)
print(result.strftime("%d.%m.%Y"))
