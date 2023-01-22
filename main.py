position = 0
while True:
    logs = open('log.log', 'r')
    logs.seek(position)

    for line in logs:
        line = device(line)
        print(line.timestamp())

    position = logs.tell()
    logs.close()
    time.sleep(10)
