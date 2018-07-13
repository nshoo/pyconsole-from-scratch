alphabet = list("abcdefghijklmnopqrstuvwxyz0123456789!: ")
lettermap = []
file = open('lettermap.txt', 'r')
lines = file.readlines()
file.close()
lettermap = [line for line in lines if line.find('=') < 0]
lettermap = [[c for c in line if c in [' ', '#']] for line in lettermap]
lettermap = [line + list((' ' * (5 - len(line)))) for line in lettermap]
lettermap = [[1 if c == '#' else 0 for c in line] for line in lettermap]
lettermap = [[lettermap[(x * 5) + i] for i in range(5)] for x in range(int(len(lettermap) / 5))]

def writeText(canvas, x, y, text, size):
    for i, c in enumerate(text):
        if c == ' ':
            pass
        else:
            letter = lettermap[alphabet.index(c)]
            if c in alphabet:
                for yo in range(5):
                    for xo in range(5):
                        if letter[yo][xo]:
                            canvas.create_rectangle(x + (xo * size) + (i * (size * 6)), y + (yo * size), x + (xo * size) + size + (i * (size * 6)), y + (yo * size) + size, fill='#222')
