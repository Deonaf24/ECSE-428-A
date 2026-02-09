from src.engine import Engine

def main() -> None:
    engine = Engine()
    while True:
        try:
            line = input()
        except EOFError:
            break

        if not line.strip():
            continue

        try:
            out = engine.execute(line)
            if out is not None:
                print(out)
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    main()
