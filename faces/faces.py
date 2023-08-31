def main():
    ask = input("")
    answer = convert(ask)
    print(answer)

def convert(str):
    str = str.replace(":)", "🙂").replace(":(", "🙁")
    return str

main()