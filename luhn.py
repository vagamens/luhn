#!/usr/bin/env python3

class Luhn:

	@staticmethod
	def calculate_sum(num):
		num = str(num)
		summ = 0
		for i in range(0,len(num)):
			j=int(num[i])
			if((i+1)%2==0):
				product = j*2
				if(product>9):
					product-=9
				j=product
			summ+=j
		return summ

	@staticmethod
	def is_valid(num):
		summ=Luhn.calculate_sum(num)
		if(summ%10==0):
			return True
		else:
			return False

	@staticmethod
	def find_checksum(num):
		summ=Luhn.calculate_sum(num)
		return int(str(summ*9)[-1])

if __name__ == '__main__':
	num1=79927398713
	num2=79927398714
	num3=7992739871
	num4=865067020379668
	print(str(num1)+": "+str(Luhn.is_valid(num1)))
	print(str(num2)+": "+str(Luhn.is_valid(num2)))
	print(str(num4)+": "+str(Luhn.is_valid(num4)))
	print(str(num3)+": "+str(Luhn.find_checksum(num3)))