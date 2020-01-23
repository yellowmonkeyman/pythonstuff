longword = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"

#Extended slice = [start, stop, step].
#There is no start, no stop but -1 indicates to start at the end and stop at the start.

longwordrev = longword[::-1]

aindex = longwordrev.find("a", 0, len(longwordrev))
eindex = longwordrev.find("e", 0, len(longwordrev))
iindex = longwordrev.find("i", 0, len(longwordrev))
oindex = longwordrev.find("o", 0, len(longwordrev))
uindex = longwordrev.find("a", 0, len(longwordrev))

print("\nLength of word = " + str(len(longwordrev)))

print("\n" + str(aindex))
print("" + str(eindex))
print("" + str(iindex))
print("" + str(oindex))
print("" + str(uindex))
print("\n")

vowellist = [aindex, eindex, iindex, oindex, uindex]
highestvowelindex = min(vowellist) + len(longwordrev)

print("Highest vowel index number = " + str(highestvowelindex))
print("\n")
