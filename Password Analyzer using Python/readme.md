# 🔐 Password Analyzer

**Password Analyzer** is a Python-based tool designed to evaluate the strength of passwords and provide actionable suggestions to improve them. It ensures users create strong, secure, and hard-to-guess passwords by analyzing multiple factors like length, complexity, and patterns.

---

## 🌟 Features
- ✅ Evaluates password strength (Weak, Moderate, Strong)
- ✅ Checks for:
  - Length (minimum 12 characters for strong passwords)
  - Presence of lowercase, uppercase, digits, and special characters
  - Common patterns like "123456", "password", or "qwerty"
  - Spaces or tabs in the password
- ✅ Provides actionable suggestions to enhance password security

---

## 🚀 Getting Started

### 1⃣ Prerequisites
- Python 3.6 or higher installed on your system.

### 2⃣ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/karan-aher/pass-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-analyzer
   ```

### 3⃣ Usage
Run the program by executing the following command:
```bash
python pass_analyzer.py
```

Enter your password when prompted, and the tool will evaluate its strength and provide feedback.

---

## 🗄️ Demo
Here's an example of the tool in action:

```
Welcome to the Password Analyzer!
Enter your password to analyze: MySecure@Password123

Password Strength: Strong
Your password is strong. Great job!
```

For a weaker password:
```
Welcome to the Password Analyzer!
Enter your password to analyze: password123

Password Strength: Weak
Suggestions to improve your password:
- Use at least 12 characters for a strong password.
- Include uppercase letters (A-Z).
- Include special characters (!@#$%^&*(),.?":{}|<>).
- Avoid common patterns like 'password', '123456', or 'qwerty'.
```

---

## 🛠️ How It Works
The tool analyzes passwords based on the following criteria:
1. **Length**: A strong password has at least 12 characters.
2. **Character Variety**: Includes lowercase, uppercase, digits, and special symbols.
3. **Common Patterns**: Avoids commonly used passwords and patterns.
4. **Whitespace**: Discourages spaces or tabs in passwords.

The password is rated as:
- `Weak` (0–3 points)
- `Moderate` (4–6 points)
- `Strong` (7+ points)

---

## 🌐 Contributions
Contributions are welcome! If you’d like to improve the tool or add new features:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your descriptive commit message"
   ```
4. Push the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request.

---

## 🛡️ License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📩 Contact
Feel free to reach out if you have questions or suggestions:
- **GitHub**: [Karan Aher](https://github.com/karan-aher)
- **Email**: mr.karanaher@gmail.com

---

### 🌟 Star this repository if you find it helpful! 😊

