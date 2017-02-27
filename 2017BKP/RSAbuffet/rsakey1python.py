# this gets the n and e from an rsa public key
# site for pycrypto

from Crypto.PublicKey import RSA

i = 0
while(i<10):
  f = open('key-'+str(i)+'.pem','r')
  r = RSA.importKey(f.read())
  print 'Key #' + str(i)
  print r.n
  print r.e
  print ""
  i = i + 1