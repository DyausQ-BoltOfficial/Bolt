# ⚡ Bolt Programming Language (`.blt`)

**Bolt** is a fast, lightweight, beginner-friendly programming language with clean, readable syntax and full access to Python's entire library ecosystem.

---

## 📥 Download & Install (v3.0)

1. Download the latest release here: **[Download Bolt_v3_Release.zip][(https://github.com] (https://github.com/DyausQ-BoltOfficial/BoltV3/releases/tag/v3.00))**
2. Extract the ZIP archive.
3. Run the one-click installer for your operating system (it sets everything up and automatically cleans up the installer files):
   * **Windows:** Open the `Windows` folder and double-click `Setup_Bolt.bat` *(installs standalone `bolt.exe` — no Python installation required)*.
   * **macOS:** Open the `Mac` folder and double-click `Setup_Mac.command` *(moves `Bolt.app` into your Applications folder)*.

---

## 🚀 Quick Start

### 1. Run a `.blt` File
Save your code in any file ending in **`.blt`** and **double-click** it—or run it from your terminal:
```bash
bolt hello.blt
```

### 2. Live Interactive Shell
Type `bolt` by itself in Command Prompt (or double-click `Bolt.app` on Mac) to launch the live `bolt>` coding sandbox.

### 3. Install Python Libraries
Use Bolt's built-in package manager to install any Python library:
```bash
bolt install requests pygame colorama
```

---

## 💻 Example Bolt Code

```python
use random

say "⚡ Welcome to Bolt!"
ask "What is your name? " -> player

let secret = random.randint(1, 10)
say f"Hello {player}, your lucky number is {secret}!"

repeat 3:
    say "Charging..."
    wait 0.5
```

---

## 📖 Documentation
A complete **`Bolt_Manual.md`** is automatically placed on your Desktop when you install Bolt.
