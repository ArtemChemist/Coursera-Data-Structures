# python3

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i, next))

        if next in ")]}":
            if  len(opening_brackets_stack)<1:
                return i+1
            prev = opening_brackets_stack.pop()
            if are_matching(prev[1],next):
                continue
            else:
                return i+1
    
    if len(opening_brackets_stack) < 1:
        return 'Success'
    else:
        return opening_brackets_stack[-1][0]+1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
