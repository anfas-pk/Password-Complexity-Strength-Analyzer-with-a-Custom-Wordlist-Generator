from analyzer.strength_checker import PasswordStrengthChecker
from analyzer.wordlist_generator import WordlistGenerator

def main():
    print("Choose an option:")
    print("1. Analyze password")
    print("2. Generate wordlist")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        pwd = input("Enter password: ")
        checker = PasswordStrengthChecker()
        strength, entropy = checker.analyze(pwd)
        print(f"[!] Strength: {strength} ({entropy:.2f} bits)")
    elif choice == '2':
        words = input("Enter base words (comma-separated): ").split(',')
        generator = WordlistGenerator()
        wordlist = generator.generate([w.strip() for w in words])
        for w in wordlist:
            print(w)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
