
## 🌐 Select your language / Chọn ngôn ngữ

* 🇬🇧 [English](#-english)
* 🇻🇳 [Tiếng Việt](#-tiếng-việt)

---

# 🇺🇸 English

# PyCool — Ultimate Python Obfuscator

> Developed by Truong Nhat Bao Nam - ktn1703

## Overview

PyCool is a next-generation Python obfuscator designed to protect Python source code against:

* static analysis
* reverse engineering
* debugging
* sandbox execution
* MITM interception
* runtime instrumentation

PyCool V4 combines:

* VM-based execution
* multi-layer encryption
* anti-analysis systems
* Unicode chaos obfuscation
* runtime payload unpacking
* high-entropy junk code generation

Inspired by:

* PyHydra
* BensOBF
* PyArmor-style protection
* malware-grade packers

---

# Features

## Dynamic Import Obfuscation

No static imports.

Uses:

```python id="g6zqqr"
__import__(''.join(map(chr,[98,97,115,101,54,52])))
```

Benefits:

* harder static analysis
* avoids simple signatures
* bypasses grep/YARA rules

---

# Unicode Variable Chaos

PyCool generates:

* Korean identifiers
* Chinese identifiers
* Fullwidth Unicode
* Invisible Unicode characters

Example:

```python id="k6e5m7"
__PyCoolHydraㅤ龍__
```

Benefits:

* destroys readability
* breaks regex tooling
---

# VM-Based Payload Execution

PyCool includes a fake virtual machine executor with:

* stack/register structures
* runtime staged decryption
* dynamic payload loading

Payload only exists at runtime.

---

# Multi-Layer Encryption Stack

Pipeline:

```text id="5v8v7x"
marshal
→ zlib
→ zlib
→ bz2
→ lzma
→ base85
→ XOR (32-byte)
→ Fisher-Yates shuffle
→ RC4
→ rolling XOR
→ base64
```

Benefits:

* high entropy
* difficult payload recovery
* difficult automated unpacking

---

# Anti-Debug Protection

Detects:

* debugpy
* pdb
* PyCharm debugger
* VSCode debugger
* tracing hooks
* suspicious stack depth
* timing manipulation

---

# Anti-VM / Anti-Sandbox

Detects:

* VMware
* VirtualBox
* QEMU
* Hyper-V
* sandbox environments

Checks:

* CPU count
* RAM size
* VM processes
* DMI vendor strings
* execution timing

---

# Anti-Hook Protection

Detects:

* requests monkey patching
* httpx hooks
* urllib3 wrappers
* instrumentation layers

Protects against:

* Frida hooks
* MITM interception
* runtime API patching

---

# Anti-Proxy / Anti-MITM

Detects:

* Burp Suite
* Fiddler
* mitmproxy
* HTTPToolkit
* Charles Proxy

---

# Hidden Anti-Analysis Layers

All anti-analysis code is:

* encoded
* compressed
* XOR protected
* dynamically executed

Nothing appears directly in plain source.

---

# Massive Junk & Dead Code Engine

Includes:

* fake crypto logic
* fake matrix operations
* dead loops
* fake lambda chains
* fake classes
* fake execution branches

20+ junk patterns.

---

# Status

⭐ 10 STARS = PUBLIC SOURCE ⭐

If this repository reaches:

```text id="x9mv9h"
10 GitHub Stars
```

The full source code of:

* PyCool 
* VM executor
* RC4 engine
* junk generator
* anti-analysis system

will be released publicly.

---

# 🇻🇳 Tiếng Việt

# PyCool — Ultimate Python Obfuscator

> được phát triển bởi Trương Nhật Bảo Nam - ktn1703

## Giới thiệu

PyCool là một Python obfuscator thế hệ mới được tạo ra để:

* bảo vệ source code
* chống reverse engineering
* chống AI deobfuscation
* chống debug
* chống sandbox
* chống MITM/proxy
* chống runtime instrumentation

PyCool kết hợp:

* Virtual Machine execution
* multi-layer encryption
* anti-analysis
* Unicode obfuscation
* runtime payload loading
* junk/dead code entropy cao

---

# Tính năng

## Dynamic Import Obfuscation

Không dùng import tĩnh.

Ví dụ:

```python id="r0s2vk"
__import__(''.join(map(chr,[98,97,115,101,54,52])))
```

Lợi ích:

* khó scan static
* khó detect signature
* khó grep bằng regex

---

# Unicode Variable Chaos

Sinh:

* tên biến tiếng Hàn
* tiếng Trung
* fullwidth unicode
* invisible unicode

Lợi ích:

* cực khó đọc
* phá regex tooling
---

# VM-Based Payload Execution

Có hệ thống VM executor giả:

* stack/register
* staged decrypt
* runtime payload loading

Payload thật chỉ tồn tại khi runtime.

---

# Multi-Layer Encryption

Pipeline:

```text id="jlwm3g"
marshal
→ zlib
→ zlib
→ bz2
→ lzma
→ base85
→ XOR 32-byte
→ shuffle
→ RC4
→ rolling XOR
→ base64
```

Lợi ích:

* entropy cực cao
* khó unpack
* khó recover payload

---

# Anti-Debug

Detect:

* debugpy
* pdb
* debugger IDE
* tracing hook
* timing attack

---

# Anti-VM / Anti-Sandbox

Detect:

* VMware
* VirtualBox
* QEMU
* Hyper-V

Kiểm tra:

* RAM
* CPU
* process VM
* DMI strings
* timing

---

# Anti-Hook

Detect:

* requests patch
* httpx hook
* urllib wrapper
* runtime instrumentation

---

# Anti-Proxy / MITM

Detect:

* Burp
* Fiddler
* mitmproxy
* HTTPToolkit

---

# Junk & Dead Code Engine

Bao gồm:

* fake crypto
* fake matrix
* dead loops
* fake lambda chains
* fake classes
* fake execution path

20+ pattern khác nhau.
---

# Status

⭐ 10 STARS = PUBLIC SOURCE ⭐

Nếu repository đạt:

```text id="2gfflo"
10 GitHub Stars
```

Toàn bộ source code:

* PyCool 
* VM executor
* RC4 engine
* junk generator
* anti-analysis system

sẽ được public.

---

# Author

PyCool
By Truong Nhat Bao Nam - ktn1703

--- 
# Contact for more:
Instagram:
```text
https://instagram.com/_kingktn
```

Tiktok:
```
https://tiktok.com/@traitimkhongcondaunuaroi
```

Link Bio:
```text
https://eboy.asia/p.n
https://kingktn.vercel.app
```
