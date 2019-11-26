N = 10
sum = 0
count = 0
print('please input 10 number:')
while count < N:
	number = float(input())
	sum = sum + number 
	count = count +1
averagen = sum / N
print("N = {}, Sum = {}" .format(N , sum))
print("Averagen = {:.2f}" .format(averagen))
