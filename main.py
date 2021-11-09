def check_palindrome(str1):
	if str1[::-1] == str1:
		return True
	return False
str1 = input()
if check_palindrome(str1) == True:
	print("Maddy says It is Palindrome")
else:
	print("Maddy says Not a palindrome")