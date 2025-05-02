def calculate_factorial(n):
    """计算一个数的阶乘"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

def main():
    number = 5
    result = calculate_factorial(number)
    print(f"{number}的阶乘是: {result}")
    
    # 简单测试
    test_numbers = [0, 1, 3, 5, 10]
    for num in test_numbers:
        print(f"{num}的阶乘是: {calculate_factorial(num)}")

if __name__ == "__main__":
    main()