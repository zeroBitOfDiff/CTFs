'''

 https://github.com/ctfs/write-ups-2014/tree/master/hack-lu-ctf-2014/wiener
 https://github.com/pablocelayes/rsa-wiener-attack/blob/master/RSAwienerHacker.py

'''

import ContinuedFractions, Arithmetic
import sys

def hack_RSA(e,n):
  '''
  
  Finds d knowing (e,n)
  applying the Wiener continued fraction attack
  
  '''
  
  # n = input("Enter e number: ")
  # e = input("Enter n number: ")
  
  frac = ContinuedFractions.rational_to_contfrac(e, n)
  convergents = ContinuedFractions.convergents_from_contfrac(frac)

  for (k,d) in convergents:

    #check if d is actually the key
    if k!=0 and (e*d-1)%k == 0:
      phi = (e*d+1)//k
      s = n - phi + 1
      # check if the equation x^2 - s*x + n = 0
      # has integer roots
      discr = s*s - 4*n
      if(discr>=0):
        t = Arithmetic.is_perfect_square(discr)
        if t!=-1 and (s+t)%2==0:
          print("Hacked!")
  
  print("-------------------------")      
  print("d = ", d)
  print("-------------------------")
          

    

# print "HERE"

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Usage:\npython %s <n-input-file> <e-input-file>" % (sys.argv[1])
		sys.exit(0)
	file1, file2 = sys.argv[1], sys.argv[2]	      
	with open(file1) as f:
	    n = int("".join([line.strip() for line in f]))
	with open(file2) as f:
		e = int("".join([line.strip() for line in f]))
	
	print hack_RSA(e, n)