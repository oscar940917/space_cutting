import sys

def max_regions(n):
    return (n**3 + 5*n + 6) // 6

def main():
    input = sys.stdin.read().strip()
    numbers = list(map(int, input.split()))
    for n in numbers:
        print(max_regions(n))
if __name__ == "__main__":
    main()
