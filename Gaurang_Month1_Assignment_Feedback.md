# Gaurang – Month 1 Assignment Feedback

## Overall Summary

Gaurang, thank you for the detailed submission. You attempted almost the full assignment and clearly invested time practicing. This is a **good sign of intent and discipline**.

At the same time, the submission shows **strong effort but weak foundations**, especially around function design, return values, syntax correctness, and logical consistency. These gaps are normal at this stage, but they **must be fixed before moving forward**.

This feedback follows the same evaluation structure used earlier so expectations remain consistent.

---

## What You Did Well ✅

### 1. Attempt Coverage
- You attempted **most questions end-to-end**
- You did not skip complex sections (loops, lists, dictionaries)
- You openly marked weak areas — this is a good learning habit

### 2. Control Flow Understanding
- `if / elif / else` logic is mostly correct
- Credit score banding and loan eligibility logic is conceptually right

### 3. Loop Usage
- You used:
  - `for` loops
  - `while` loops
- You understand iteration over lists and conditions inside loops

### 4. Willingness to Experiment
- You tried different approaches instead of leaving blanks
- This is important for long-term growth

---

## Issues That Must Be Fixed ❌

### 1. Functions: `print` vs `return` (Critical)

You frequently used `print()` where `return` was required.

❌ Example:
```python
def square(num):
    print(num**2)
```

✅ Correct:
```python
def square(num):
    return num**2
```

Why this matters:
- `print()` only displays output
- `return` makes functions reusable and testable
- Real-world Python code **depends on return values**

---

### 2. Syntax Errors (Blocking Issue)

Some parts of the submission **will not run at all**.

❌ Examples:
```python
return bonus = salary * 0.10
student_profile ={name:"Gaurang"}
Expect IndexError:
```

These indicate:
- Code not executed before submission
- Copy-paste without verification

**Rule:** If Python throws an error, the answer is incomplete.

---

### 3. Logical Errors

❌ Example:
```python
def calculate_total_loan_amount(loan_amounts):
    total = 0
    for amount in loan_amounts:
        total += amount
    return amount
```

Correct logic:
```python
return total
```

Mistakes like this show:
- Weak tracking of variables
- Not validating output against intent

---

### 4. Incomplete Implementations

Some functions return **only the first matching value** instead of all matches.

❌ Example pattern:
```python
return application["application_id"]
```

Expected:
- Return a **list of results**
- Not a single early exit

---

### 5. Inconsistent Naming & Case Sensitivity

Issues like:
- `"Approved"` vs `"approved"`
- `loan_status` vs `status`

These cause **silent logical bugs** and must be avoided.

---

## Evaluation Summary

| Area | Score |
|---|---:|
| Effort & Coverage | 8 / 10 |
| Loops & Conditions | 7 / 10 |
| Functions & Returns | 5 / 10 |
| Syntax Correctness | 5 / 10 |
| Code Quality | 5 / 10 |
| **Overall** | **6 / 10** |

---

## Mandatory Action Items Before Month 2 🚨

You must complete the following before moving ahead:

1. Rewrite **at least 5 functions** using only `return`, no `print`
2. Fix all syntax errors and re-run the script end-to-end
3. Reattempt:
   - Total loan calculations
   - Approved loan summaries
   - High-value loan filtering
4. Be able to **explain every line you submit**

Using tools like ChatGPT is fine **only if you understand the output fully**.

---

## Final Note

You are putting in effort — that is good.  
Now the focus must shift to **precision, correctness, and clarity**.

Once these fundamentals are fixed, your progress will accelerate quickly.

**Good effort. Foundation strengthening is the next priority.**
