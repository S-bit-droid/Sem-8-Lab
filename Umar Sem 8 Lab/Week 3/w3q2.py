def count_vowels(s):
    s=s.lower()
    count=0
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u': count+=1
    return count

s=input('Enter a string:')
res=count_vowels(s)
print('Number of vowels in entered string:',res)