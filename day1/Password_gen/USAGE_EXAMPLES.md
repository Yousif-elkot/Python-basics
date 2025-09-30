# 🔐 Password Generator - Usage Examples

This document provides comprehensive examples of how to use the Password Generator CLI tool.

## 📋 **Quick Reference**

```bash
# Basic usage
python Password_gen.py                          # Default: 12 characters, all types

# Help and version
python Password_gen.py -h                       # Show help message
python Password_gen.py --help                   # Show detailed help
```

---

## 🎯 **Basic Examples**

### **Default Password Generation**
```bash
$ python Password_gen.py

Generated 1 password(s) with length 12:
Character types: Lowercase Uppercase Digits Symbols
Password strength: Very Strong
----------------------------------------
1: Mk7#vB2$nQ9x
```

### **Custom Length**
```bash
$ python Password_gen.py -l 16

Generated 1 password(s) with length 16:
Character types: Lowercase Uppercase Digits Symbols
Password strength: Excellent
----------------------------------------
1: 9mX#kL2$vB7@nQ5z
```

### **Multiple Passwords**
```bash
$ python Password_gen.py -c 5

Generated 5 password(s) with length 12:
Character types: Lowercase Uppercase Digits Symbols
Password strength: Very Strong
----------------------------------------
1: 8kL#mN2$vX9q
2: R7@zB4%nM6&kP
3: Q5!vC8*mL2$nX
4: N9#kP7@vB3%mZ
5: L6$mX4*nQ8!vC
```

---

## 🔧 **Character Type Control**

### **No Symbols (Alphanumeric Only)**
```bash
$ python Password_gen.py --no-symbols

Generated 1 password(s) with length 12:
Character types: Lowercase Uppercase Digits
Password strength: Strong
----------------------------------------
1: K7mN2vB9xQ5z
```

### **No Uppercase (Lowercase + Digits + Symbols)**
```bash
$ python Password_gen.py --no-uppercase

Generated 1 password(s) with length 12:
Character types: Lowercase Digits Symbols
Password strength: Strong
----------------------------------------
1: k7#mn2$vx9q
```

### **Letters Only (No Digits or Symbols)**
```bash
$ python Password_gen.py --no-digits --no-symbols

Generated 1 password(s) with length 12:
Character types: Lowercase Uppercase
Password strength: Moderate
----------------------------------------
1: mKvBnQxLzPmN
```

### **Numbers Only**
```bash
$ python Password_gen.py --no-lowercase --no-uppercase --no-symbols

Generated 1 password(s) with length 12:
Character types: Digits
Password strength: Weak
----------------------------------------
1: 729563840172
```

---

## 🛡️ **Security Options**

### **Exclude Ambiguous Characters**
```bash
$ python Password_gen.py --no-ambiguous

Generated 1 password(s) with length 12:
Character types: Lowercase Uppercase Digits Symbols
(Ambiguous characters excluded)
Password strength: Very Strong
----------------------------------------
1: Mk7#vB2$nQ9x
```
*Note: Excludes `I`, `l`, `1`, `O`, `0` for better readability*

### **Disable Variety Enforcement**
```bash
$ python Password_gen.py --no-variety

Generated 1 password(s) with length 12:
Character types: Lowercase Uppercase Digits Symbols
Password strength: Strong
----------------------------------------
1: kkkkkkk7#vBn
```
*Note: May generate passwords with only some character types*

---

## ⚡ **Advanced Combinations**

### **Long, High-Security Password**
```bash
$ python Password_gen.py -l 32 --no-ambiguous

Generated 1 password(s) with length 32:
Character types: Lowercase Uppercase Digits Symbols
(Ambiguous characters excluded)
Password strength: Excellent
----------------------------------------
1: Mk7#vB2$nQ9xR4@kL6%mN8*vB3!nX5z
```

### **Multiple Secure Passwords for Team**
```bash
$ python Password_gen.py -l 16 -c 10 --no-ambiguous --no-symbols

Generated 10 password(s) with length 16:
Character types: Lowercase Uppercase Digits
(Ambiguous characters excluded)
Password strength: Excellent
----------------------------------------
1: Mk7vB2nQ9xR4kL6
2: vB9xQ5zR7kM3nP8
3: nQ9xR4kL6mN8vB2
4: Q5zR7kM3nP8vB9x
5: R4kL6mN8vB2nQ9x
6: kM3nP8vB9xQ5zR7
7: L6mN8vB2nQ9xR4k
8: nP8vB9xQ5zR7kM3
9: N8vB2nQ9xR4kL6m
10: vB9xQ5zR7kM3nP8
```

### **Short Passwords Without Variety**
```bash
$ python Password_gen.py -l 6 --no-variety --no-symbols

Generated 1 password(s) with length 6:
Character types: Lowercase Uppercase Digits
Password strength: Moderate
----------------------------------------
1: Mk7vB2
```

---

## ❌ **Error Examples**

### **All Character Types Disabled**
```bash
$ python Password_gen.py --no-lowercase --no-uppercase --no-digits --no-symbols

Error: Character set is empty. Enable at least one character type.
```

### **Length Too Short for Variety**
```bash
$ python Password_gen.py -l 2

Error: Length must be at least 4 to ensure variety.
```

### **Valid Short Password (Variety Disabled)**
```bash
$ python Password_gen.py -l 2 --no-variety

Generated 1 password(s) with length 2:
Character types: Lowercase Uppercase Digits Symbols
Password strength: Very Weak
----------------------------------------
1: K7
```

---

## 🎯 **Use Case Examples**

### **Website Registration**
```bash
# Strong, readable password for manual typing
python Password_gen.py -l 14 --no-ambiguous --no-symbols
```

### **Database Credentials**
```bash
# High-security password for automated systems
python Password_gen.py -l 24 --no-ambiguous
```

### **Temporary Passwords**
```bash
# Multiple short passwords for temporary access
python Password_gen.py -l 8 -c 5 --no-symbols
```

### **API Keys Simulation**
```bash
# Long alphanumeric strings
python Password_gen.py -l 40 --no-symbols --no-ambiguous
```

---

## 📊 **Password Strength Guide**

| Length | Character Types | Strength Rating | Use Case |
|--------|----------------|----------------|----------|
| 4-7    | 1-2 types      | Very Weak - Weak | Not recommended |
| 8-11   | 2-3 types      | Moderate - Strong | Basic accounts |
| 12-15  | 3-4 types      | Strong - Very Strong | Most applications |
| 16+    | 3-4 types      | Very Strong - Excellent | High security |

---

## 🔧 **Tips and Best Practices**

1. **For manual typing**: Use `--no-ambiguous` to avoid confusion
2. **For copy/paste**: Include all character types for maximum security
3. **For databases**: Use longer passwords (16+ characters)
4. **For teams**: Generate multiple passwords with `-c` flag
5. **For systems**: Use `--no-variety` only when forced by legacy requirements

---

## 🚀 **Integration Examples**

### **Batch Script Generation**
```bash
# Generate 100 passwords and save to file
python Password_gen.py -l 16 -c 100 --no-ambiguous > passwords.txt
```

### **Pipeline Usage**
```bash
# Use in shell scripts
PASSWORD=$(python Password_gen.py -l 12 --no-symbols | tail -1 | cut -d' ' -f2)
echo "Generated password: $PASSWORD"
```