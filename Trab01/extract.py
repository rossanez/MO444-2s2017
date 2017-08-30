import numpy as np

filename = 'log.txt'
file = open(filename, 'rt')

extracted_array = []
with file as f:
    for line in f:
        line = line.strip()
        if "Avg. loss:" in line:
            tmp = line.split("Avg. loss:")
            loss = tmp[1].split(':')[0]
            extracted_array.append(loss)
        elif "2 -- Epoch 1" in line:
            break

print('avg_losses = [%s]' % ','.join(extracted_array))

