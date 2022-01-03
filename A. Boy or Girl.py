# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
def main():
    s1 = input()  # String.
    s1 = dict.fromkeys(s1)  # Convert it to dictionary to remove duplicates.

    if len(s1) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    main()