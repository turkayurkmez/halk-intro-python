def log_register(*messages, **settings):
    import datetime

    level = settings.get("level","INFO")
    time_stamp = settings.get("time",True)
    file = settings.get("file",None)

    if time_stamp:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prefix = f"[{time}] [{level}]"
    else:
        prefix = f"[{level}]"

    full_message = f"{prefix} {' '.join(map(str,messages))}"

    print(full_message)
    if file:
        print("log dosyasına kaydedildi")    
    print()


