s = input("Enter a string: ")
words = s.split()
words.reverse()
print(" ".join(words))

# split() → String चे शब्द वेगळे करून List बनवते
# reverse() → त्या List चा क्रम उलटा करते
# join() → List मधील शब्द पुन्हा Space देऊन String मध्ये जोडते