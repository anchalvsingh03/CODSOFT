import random  
import string  
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    if length < 1:
        return "Password length must be at least 1."
    character_set = ""
    if use_uppercase:
        character_set += string.ascii_uppercase  
    if use_lowercase:
        character_set += string.ascii_lowercase 
    if use_digits:
        character_set += string.digits  
    if use_special:
        character_set += string.punctuation  
    if not character_set:
        return "You must select at least one character type."
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter Length of the password: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return 
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    print("Generated Password:" , password)
if __name__ == "__main__":
    main()