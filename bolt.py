import sys, os, subprocess
try:
    import requests, colorama, bs4, fastapi
except ImportError:
    pass

def transpile(bolt_code):
    bolt_code = bolt_code.lstrip("\ufeff")
    py_lines = []
    for line in bolt_code.splitlines():
        indent = line[:len(line) - len(line.lstrip())]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            py_lines.append(line)
            continue
        if stripped.startswith("use "):
            stripped = "import " + stripped[4:]
        elif stripped.startswith("from ") and " use " in stripped:
            stripped = stripped.replace(" use ", " import ", 1)
        elif stripped.startswith("func "):
            stripped = "def " + stripped[5:]
        elif stripped.startswith("say "):
            arg = stripped[4:].strip()
            stripped = f"print({arg})" if not (arg.startswith("(") and arg.endswith(")")) else f"print{arg}"
        elif stripped.startswith("say("):
            stripped = "print" + stripped[3:]
        elif stripped.startswith("ask ") and "->" in stripped:
            prompt, var = stripped[4:].rsplit("->", 1)
            stripped = f"{var.strip()} = input({prompt.strip()})"
        elif stripped.startswith("let "):
            stripped = stripped[4:]
        elif stripped.startswith("repeat ") and stripped.endswith(":"):
            count = stripped[7:-1].strip()
            stripped = f"for _ in range({count}):"
        elif stripped.startswith("wait "):
            secs = stripped[5:].strip()
            stripped = f"__import__('time').sleep({secs})"
        elif stripped == "cls":
            stripped = "__import__('os').system('cls' if __import__('os').name == 'nt' else 'clear')"
        py_lines.append(indent + stripped)
    return "\n".join(py_lines)

def start_repl():
    print("Bolt v3.0 Interactive Shell (Type 'exit' to quit)")
    exec_globals = {"__name__": "__main__"}
    buffer = []
    while True:
        try:
            prompt = "... " if buffer else "bolt> "
            line = input(prompt)
            if not buffer and line.strip() in ("exit", "quit"):
                break
            if line.endswith(":") or buffer:
                if line.strip() == "" and buffer:
                    code = "\n".join(buffer)
                    buffer.clear()
                    exec(transpile(code), exec_globals)
                else:
                    buffer.append(line)
                continue
            if line.strip():
                compiled = transpile(line)
                try:
                    res = eval(compiled, exec_globals)
                    if res is not None:
                        print(res)
                except SyntaxError:
                    exec(compiled, exec_globals)
        except KeyboardInterrupt:
            buffer.clear()
            print("\n[Interrupted]")
        except Exception as e:
            buffer.clear()
            print(f"[Bolt Error] {e}")

def main():
    if len(sys.argv) < 2:
        start_repl()
        return
    if sys.argv == "install" and len(sys.argv) >= 3:
        subprocess.check_call(["pip", "install", *sys.argv[2:]])
        return
    if sys.argv == "list":
        subprocess.call(["pip", "list"])
        return
    file_path = sys.argv
    if not os.path.exists(file_path):
        print(f"[Bolt Error] File not found: {file_path}")
        return
    with open(file_path, "r", encoding="utf-8-sig") as f:
        code = f.read()
    exec_globals = {"__name__": "__main__", "__file__": file_path}
    try:
        exec(transpile(code), exec_globals)
    except Exception as e:
        print(f"\n[Bolt Runtime Error] {e}")

if __name__ == "__main__":
    main()