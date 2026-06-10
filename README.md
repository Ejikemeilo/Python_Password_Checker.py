# Python Password Strength Checker

A command-line tool that evaluates the strength of a password in real time and gives actionable tips to improve it.

**Author:** Ejikeme Cyril Ilo  
**Track:** DecodeLabs Cybersecurity Industrial Training — Batch 2026

---

## What It Does

- Checks a password against 4 security rules
- Returns a strength rating: **Weak**, **Medium**, or **Strong**
- Gives specific tips on what to improve if the password is not strong
- Loops so you can test multiple passwords in one session
- Rejects passwords shorter than 5 characters before even checking

## The 4 Rules

| Rule | Requirement |
|------|-------------|
| Length | At least 8 characters |
| Uppercase | Contains at least one uppercase letter (A–Z) |
| Digit | Contains at least one number (0–9) |
| Symbol | Contains at least one special character (e.g. `!@#$%`) |

## Strength Ratings

| Score | Rating |
|-------|--------|
| 1 or below | Weak — very easy to crack |
| 2 – 3 | Medium — okay but can be stronger |
| 4 | Strong — secure |

## How to Run

```bash
python Python_Password_Checker.py
```

You will be prompted to enter a password. Type `quit` to exit.

## Example Output

```
=== Ejikeme_Ilo Password Strength Checker ===

Enter your password (or type 'quit' to exit): hello

Strength: WEAK ❌ - Your password is very easy to crack!

💡 Tips to improve your password:
- Add uppercase letters (e.g. A, B, C)
- Add numbers (e.g. 1, 2, 3)
- Add symbols (e.g. !, @, #)
- Make it at least 8 characters long
```

## Files

| File | Description |
|------|-------------|
| `Python_Password_Checker.py` | Main password checker script |

---

*Powered by DecodeLabs · Greater Lucknow, India · decodelabs.tech*
