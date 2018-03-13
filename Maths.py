"""
Prime numbers from 0 to 100
"""
def prime_numbers():
	for num in range(2,101):
		if all(num%i!=0 for i in range(2,num)):
			print (num)
    
    
"""
First n prime numbers
"""
def primes(n):
	prime = [2]
	attempt = 3
	while len(prime) < n:
		if all(attempt % p != 0 for p in prime):			
			prime.append(attempt)
		attempt += 2	
	return prime
  
  """"
  Sum of first n number of even fibonacci series
  """
  
  def sum_even_fibonacci(n):
    i=1
    count=0
    fibonacci_sum=0
    fibonacci_series = [1,1]
    sum_no = 1
    while count<=n:
        temp = sum_no + fibonacci_series[i-1]
        fibonacci_series.append(temp)
        sum_no = temp
        i+=1
        if sum_no%2==0:
            count+=1
            fibonacci_sum = fibonacci_sum + sum_no
    print("The sum of first n even fibonacci numbers is ",fibonacci_sum)

"""
Largest palindrome of the product of two 3-digit numbers
"""
def largest_palindrome():
    palindromes=[]
    x=999
    y=99
    while x>y:
        for i in range(x,y, -1):
            product = x*i
            string = str(product)
            if (string == string[::-1]):
                palindromes.append((product,x,i))
                y=i
                break
        x-=1
    largest_palindrome = max(palindromes)
    print("The largest palindrome and the two numbers are:",largest_palindrome)
    return(largest_palindrome)


