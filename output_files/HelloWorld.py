# Function to match character 
def check(s1, s2): 
    mp = {}
    for char in s1:
        mp[char] = mp.get(char, 0) + 1
    for char in s2:
        if char in mp and mp[char] > 0:
            return True
    return False

# Driver code 
s1 = "geeksforgeeks"
s2 = "geeks"

# Find if there is a common subsequence 
yes_or_no = check(s1, s2)

if yes_or_no:
    print("Yes")
else:
    print("No")