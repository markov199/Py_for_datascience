from datetime import datetime

x = datetime.now()
txt = f"Seconds since January 1, 1970:{x.timestamp():,} or {x.timestamp():.2e} in scientific notation"
print(txt)

print(x.strftime("%b %d %Y"))