import collections
S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}

S_dict = collections.defaultdict(list)
for i in range(len(S)):
        S_dict[S[i]].append(i)

print(S_dict)
w = False
for word in sorted(D, key=lambda w: len(w), reverse=True):
	pos = 0
	for i,letter in enumerate(word):
		if letter not in S_dict:
			break
		possible = [p for p in S_dict[letter] if p>=pos]
		if not possible:
			break
		pos = possible[0] + 1
		if i == len(word)-1:
			w=word

	if w:
		print(w, " is largest subsequence of ", S)
		break
if not w:
	print("No subsequence")