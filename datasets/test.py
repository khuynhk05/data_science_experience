import bcrypt

f  =open("./salt.txt", 'r')
salt = f.read()

password="819574217efc4df6b9aaa87a8fe207a8"
hashed=bcrypt.hashpw(password, salt)
print ("%s, %s" % (password, hashed))

password="11566479e5c75d691a11f18e9093fe72a0cc8df7c6554717"
hashed=bcrypt.hashpw(password, salt)
print ("%s, %s" % (password, hashed))

password="d2c1a23952234d0a8c92e6f6a69bc2a4"
hashed=bcrypt.hashpw(password, salt)
print ("%s, %s" % (password, hashed))

password="f304ec2719f2b4a2ab82ae975cf498728e9b99bc47254429"
hashed=bcrypt.hashpw(password, salt)
print ("%s, %s" % (password, hashed))


