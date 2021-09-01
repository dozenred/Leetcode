number = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
          "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
while (1):
    x_int = int(input())
    for i in range(x_int):
        x_str = input()
        start = 0
        n0 = x_str.count('Z')
        n2 = x_str.count('W')
        n4 = x_str.count('U')
        n6 = x_str.count('X')
        n8 = x_str.count('G')

        n1 = x_str.count('O') - n0 - n2 - n4
        n3 = x_str.count('T') - n2 - n8
        n5 = x_str.count('F') - n4
        n7 = x_str.count('S') - n6
        n9 = x_str.count('I') - n5 - n6 - n8
        result = '0' * n8 + '1' * n9 + '2' * n0 + '3' * n1 + '4' * n2 + '5' * n3 + '6' * n4 + '7' * n5 + '8' * n6 + '9' * n7
        print(result)