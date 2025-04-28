import time


ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*.-_'
MIN_LENGTH = 4
MAX_LENGTH = 8
PASSWORD = "ABC12"


def generate_next_symbol(symbol):
    if symbol == ALPHABET[-1]:
        return False
    current_symbol_index = ALPHABET.index(symbol)
    return ALPHABET[current_symbol_index + 1]


def generate_next_string(password):
    position = len(password) - 1
    while True:
        symbol = generate_next_symbol(password[position])
        if symbol:
            return password[:position] + symbol + password[position+1:]
        password = password[:position] + ALPHABET[0] + password[position+1:]
        position -= 1
        if position < 0:
            break
    return False



def check_all_combinations(length):
    password = ALPHABET[0] * length
    while True:
        if password == PASSWORD:
            print(password)
            return True
        password = generate_next_string(password)
        if not password:
            break
    return False


def main():
    length = MIN_LENGTH
    while length <= MAX_LENGTH:
        print(f"length: {length}")
        start = time.monotonic()
        password_match = check_all_combinations(length)
        end = time.monotonic()
        print(f"time: {end-start}")
        if password_match:
            break
        length += 1


if __name__ == "__main__":
    main()
