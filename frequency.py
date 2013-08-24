# frequency.py is to calculate the letter frequency of a essay.
# The sample imported here is from http://norvig.com/big.txt
# The result may not be simliar to what you read from Wikipedia,
# but you can do it on your own and import different essays.
# BTW, what you see is NOT what I input originally, it's simplified.

words = file('source.txt').read().lower()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def run():
    material = ''.join(words.split())
    leng = len(material) * 1.0

    for letter in alphabet:
	print '%s %.2f%i' % (letter, (material.count(letter)/leng*100))

if __name__ == '__main__':
    print "Jing Guo code the program, it's Ver 1.0, you are free to use."
    run()


# Wikipedia link: http://en.wikipedia.org/wiki/Letter_frequency
# You would see the result like this:

# a 7.67
# b 1.37
# c 2.72
# d 4.05
# e 11.91
# f 2.27
# g 1.82
# h 5.54
# i 6.87
# j 0.12
# k 0.62
# l 3.73
# m 2.39
# n 6.93
# o 7.27
# p 1.86
# q 0.09
# r 5.81
# s 6.29
# t 8.65
# u 2.61
# v 0.98
# w 1.89
# x 0.18
# y 1.70
# z 0.07
