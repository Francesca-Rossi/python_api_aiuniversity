import sys
def sum(firstVar,secondVar):
    try:
        somma(firstVar, secondVar)
    except Exception as e:
        print(e)

def somma(firstVar, secondVar):
    return int(firstVar) + int(secondVar)
print(sum(sys.argv[1],sys.argv[2]))
sys.stdout.flush()


