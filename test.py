fruits = ["apple", "banana", "pineapple", "watermelon", "orange",
          "durian", "mango", "peach", "grape", "dragonfruit"]

fruits2 = [fruit[::-1] for fruit in fruits[::-1]]
print(fruits2)

fruitsCapital =  [fruits[0].upper() + fruits[1:] for fruit in fruits if  fruits[1] == 'a']
print(fruitsCapital)

[ n for n in range(0, 50) if '7' in str(n) ]
# Output = 7, 17, 27, 37, 47 

arr = "abcd"

i = 0
arr2 = [arr[i] + str(i) for i in range(len(arr))]
print(arr2)

colors = ["black", "white", "gray"]
sizes = ["XS", "S", "M", "L", "XL"]

ColorsXSize =  [(color, size) for color in colors for size in sizes if color != 'white' and size != 'M']
print(ColorsXSize)

# 7) This produces all white shirts of all sizes 
# 8) tshirts2 = [(t[0], t[1], i) for i, t in enumerate(tshirts)] can't explain 

#9) b 
# 10 ) d 
# 11) True
# 12) A-

grades = { "Tom": "A", "Mary": "B", "Alex": "C", "John": "B", "Peter": "F" }
grades2 = {}

for grade in grades:
    if grade[1] not in grades2:
        grades2[1] = grade[1]
    grades2.add(grades[0])



print(grades2)

