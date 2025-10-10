# 📋 V.P.C.R. Method - Quick Reference Card

**V.P.C.R. = Visualize, Pseudocode, Code, Refine**

**Purpose:** A repeatable process for solving any coding problem systematically.

---

## 📝 The 4 Steps

### 1️⃣ Visualize (10-15 min)

**Goal:** Understand the problem completely before touching code.

**What to do:**
- [ ] Draw a diagram or flowchart
- [ ] Identify inputs (what goes in?)
- [ ] Identify outputs (what comes out?)
- [ ] Map the transformation steps
- [ ] Sketch example cases (especially edge cases)

**Tools:**
- Paper and pen
- Whiteboard
- Markdown diagrams in README
- Draw.io or Excalidraw

**Example (Backup Script):**
```
Input: source_dir, dest_dir, backup_name
       ↓
Check source exists? → No → Error
       ↓ Yes
Check dest exists? → No → Create it
       ↓ Yes
Generate filename with timestamp
       ↓
Create tar.gz archive
       ↓
Get file size
       ↓
Output: Success message + filename + size
```

---

### 2️⃣ Pseudocode (15-20 min)

**Goal:** Write the logic in plain language before actual syntax.

**What to do:**
- [ ] Write the algorithm in English (or your language)
- [ ] Use indentation to show structure
- [ ] Include all major steps and decisions
- [ ] Identify edge cases and error handling
- [ ] Don't worry about syntax - clarity over correctness

**Format:**
```
function backup(source, dest, name):
    if source does not exist:
        show error and exit
    
    if dest does not exist:
        create dest
        if creation failed:
            show error and exit
    
    timestamp = current date in YYYYMMDD_HHMMSS format
    filename = dest + "/" + name + "_" + timestamp + ".tar.gz"
    
    run tar command to compress source into filename
    if tar failed:
        show error and exit
    
    size = get file size of filename
    print success message with filename and size
```

**Tips:**
- Use simple verbs: "check", "create", "loop", "compare"
- Avoid language-specific terms (no `if/else`, use "if...otherwise")
- Think about what a human would do step-by-step

---

### 3️⃣ Code (60-90 min)

**Goal:** Translate pseudocode into actual, working code.

**What to do:**
- [ ] Start with function signatures and structure
- [ ] Translate pseudocode line-by-line
- [ ] Code in small chunks (5-10 lines at a time)
- [ ] Test each chunk before moving on
- [ ] Keep it simple and readable

**Best practices:**
```python
# Good: Matches pseudocode, clear intent
if not os.path.exists(source_dir):
    error_exit(f"Source not found: {source_dir}")

# Bad: Over-engineered, hard to verify against pseudocode
try:
    assert os.path.exists(source_dir), "Source missing"
except AssertionError as e:
    sys.stderr.write(str(e))
    sys.exit(1)
```

**Tips:**
- Keep your pseudocode visible while coding
- Add comments that reference pseudocode steps
- Don't "optimize" yet - make it work first
- Test frequently (every 10-20 lines)

---

### 4️⃣ Refine (30-45 min)

**Goal:** Make it robust, clean, and production-ready.

**What to do:**
- [ ] Test with normal inputs
- [ ] Test with edge cases (empty, null, boundary values)
- [ ] Test with invalid inputs (wrong types, out of range)
- [ ] Add error handling for unexpected cases
- [ ] Add comments where logic is non-obvious
- [ ] Refactor for clarity (better variable names, extract functions)
- [ ] Check code style (PEP 8 for Python, shellcheck for Bash)
- [ ] Write documentation (docstrings, README)

**Testing checklist:**
```markdown
- [ ] Happy path (normal valid input)
- [ ] Empty input
- [ ] Single item input
- [ ] Large input
- [ ] Invalid type (if applicable)
- [ ] Boundary values (0, -1, max)
- [ ] Special characters or spaces in strings
- [ ] Non-existent files/paths
- [ ] Permission issues
```

**Refactoring checklist:**
```markdown
- [ ] Variable names are descriptive
- [ ] Functions do one thing
- [ ] No magic numbers (use constants)
- [ ] No duplicated code
- [ ] Error messages are helpful
- [ ] Comments explain "why", not "what"
```

---

## 🎯 When to Use V.P.C.R.

**Always use for:**
- ✅ Any new project (even small scripts)
- ✅ Contest problems (ICPC, LeetCode)
- ✅ Interview coding challenges
- ✅ Debugging complex issues (go back to Visualize)

**Optional for:**
- Quick one-liners or simple fixes
- Copying example code for learning
- Boilerplate setup tasks

---

## ⏱️ Time Allocation

| Step | Time | % of Total |
|------|------|-----------|
| Visualize | 10-15 min | 8-10% |
| Pseudocode | 15-20 min | 12-15% |
| Code | 60-90 min | 50-60% |
| Refine | 30-45 min | 20-25% |
| **Total** | **2-2.5 hours** | **100%** |

**Important:** Don't skip Visualize and Pseudocode to save time! They actually SAVE time by preventing wrong approaches.

---

## 🚫 Common Mistakes

### ❌ Mistake #1: Jumping straight to code
**Problem:** You waste time on wrong approaches, get stuck, or write unmaintainable code.
**Solution:** Force yourself to do Visualize and Pseudocode first, even if you "already know" the solution.

### ❌ Mistake #2: Making pseudocode too detailed
**Problem:** It becomes actual code in disguise, defeating the purpose.
**Solution:** Use plain language, avoid syntax. If you're typing `if`, `for`, brackets, you've gone too far.

### ❌ Mistake #3: Skipping Refine because "it works"
**Problem:** Code that "works" on happy path fails in production, or is unreadable for others (including future you).
**Solution:** Testing edge cases is NOT optional. Spend the full 30-45 minutes on Refine.

### ❌ Mistake #4: Not writing down Visualize and Pseudocode
**Problem:** Doing it "in your head" doesn't count - you forget details, skip steps.
**Solution:** Write it in your README, in comments, on paper - just write it down!

---

## 📚 V.P.C.R. Examples in This Repo

| File | V.P.C.R. Documented? | Complexity |
|------|---------------------|------------|
| `day8/README.md` | ✅ Full example | Medium |
| `day7/challenge1.py` | ⚠️ Only code | Easy |
| `day3/task_queue.py` | ⚠️ Partial | Medium |

**Your goal:** Every new project should have full V.P.C.R. documentation like `day8/README.md`.

---

## 🎓 V.P.C.R. Template for Your README

```markdown
# Day X: [Topic]

## Project: [Name]

### V.P.C.R. Method

#### 1. Visualize (10-15 min)

**Input:**
- [What goes in?]

**Output:**
- [What comes out?]

**Flow:**
\`\`\`
[Draw the steps]
\`\`\`

#### 2. Pseudocode (15-20 min)

\`\`\`
[Write the logic in plain English]
\`\`\`

#### 3. Code

See: [filename.py]

#### 4. Refine

**Testing checklist:**
- [ ] Test case 1
- [ ] Test case 2
- [ ] Edge case 1

**Improvements made:**
- [What did you improve?]
\`\`\`

---

## 💡 Pro Tips

1. **Visualize on paper first** - Screen distracts, paper focuses
2. **Say pseudocode out loud** - If it sounds weird to say, it's too detailed
3. **Code in baby steps** - Write 5 lines, run it, write 5 more
4. **Refine ruthlessly** - Your first working version is NOT the final version
5. **Compare with others** - After you solve it, look at other solutions to learn patterns

---

## 🎯 The V.P.C.R. Mindset

**Before V.P.C.R.:**
> "I need to solve this problem. Let me start typing code and figure it out as I go."
> Result: Stuck, confused, spaghetti code, many do-overs.

**After V.P.C.R.:**
> "I need to solve this problem. Let me first understand it visually, then plan the logic, then implement step-by-step, then polish it."
> Result: Clear path, confident execution, clean code, efficient process.

---

## 📖 Further Reading

- **Day 8 README** (`day8/README.md`) - Full worked example
- **60-Day Roadmap** - V.P.C.R. is mandatory for all projects
- **How to Solve It** by George Pólya - Classic problem-solving framework (V.P.C.R. is inspired by this)

---

**Remember:** V.P.C.R. is not optional. It's THE method. Every project. Every time. This is how engineers think.

**Print this file and keep it next to your computer.** 🖨️

---

**Quick V.P.C.R. Checklist:**
- [ ] ✏️ Visualize (draw it)
- [ ] 📝 Pseudocode (write it in English)
- [ ] 💻 Code (translate it to syntax)
- [ ] ✨ Refine (test it, polish it)
