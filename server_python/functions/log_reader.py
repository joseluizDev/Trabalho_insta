def reader(last):
    # get logs
    logs = []
    # get last log number
    last = last
    # get logs
    with open('logs/log_de_criacao.txt', 'r') as f:
        atualLine = 0
        for line in f:
            line = line.replace('\n', '')
            line = line.strip()
            if(line != ''):
                if atualLine >= last:
                    logs.append(line)
                atualLine += 1
                with open('logs/log_de_criacao.txt', 'r') as fr:
                    lines = fr.readlines()
                    with open('logs/log_de_criacao.txt', 'w') as fw:
                        for linesw in lines:

                            if linesw == line:
                                fw.write(linesw)
    return logs
