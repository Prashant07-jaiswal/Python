book = "Alchemist"
rev = ""
for i in book:
    rev = i + rev  # 1. rev+i = ""+"A" = "A" , i+rec = "A"+"" = "A"
print(rev)         # 2. rev+i = "A"+"l" = "Al" , i+rev = "l"+"A" = "lA"