# 1. Background
## 1.1 Aims and objectives
The aim of this Python project is to use Object-Orientated Programming in mitigating a security issue for an appointment and scheduling management system (ASMIS) of Queens Medical Centre. The ASMIS is a cloud-based software as a service (Saas) and can be access through mobile and desktop devices. The ASMIS contains basic information related to patient’s registration details, appointments and preferred medical specialist as well as the medical clinic’s administrative staff who maintain the availability and scheduling of the medical specialists. Although the patient’s and clinic’s core information and records are isolated from AMSIS, threat actors can obtain user's Personal Identifiable Information (PII).

## 1.2 Threats
The main threats to the ASMIS are to use HTTPS spoofing and IDN homograph attacks to fake the ASMIS landing page with a login portal that can harvest user’s credentials as well as brute force attacks on the password Login to gain access. To mitigate these threats, Phillips (2018) advises to implement two classes for web login which will help validate the password and username combination.

1. Authenticator class: ensuring the user is who they say they really are.
2. Authorizer class: ensuring the authenticated user has correct access to certain functions.

However, this programme will focus on authentication as it only relates to registering and logging in of patient’s username and password.


## 3. Passwords and hashing
When dealing with passwords, there are various elements that need to be considered such as password complexity, length, history, expiration date, and encryption. The authenticator class looks at password encryption, password length and complexity.

* If len(password) < 5	= 			password must be six or more characters
* If not any(char.isdigit()	 = 		password must have at least one numeral
* If not any(char.isupper()	 =		password must have one uppercase letter
* If not any(char.islower()	 =		password must have one lowercase letter


The below examples shows if a user inputs a password of less than five characters it will be rejected, and it must include an alpha-numeric password with a lower and upper letter. For example, ‘g1234’ would be rejected, whereas ‘Ab4521421’ would be accepted. 

![rejected accept](https://github.com/JonnyAsh/OOP_ASMIS/blob/67a55d35199aa14fb51effb24afb3b8f9a1e01c9/images/accept%20reject.png)

Once a user signs up with a username and password, it is stored in the patient’s text file. Here it is stored in string text which can be easily read if accessed by a threat actor. To improve the security and confidentiality of the patient’s PII, the user class uses the imported Hashlib library to encode the password string. The Hashlib takes the user’s password and hashes it using sha256 constructor which results in a hash value.

```html
def _encrypt_pw(self, password):
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string) .hexdigest()


```

## 3. Patient’s username and password database
This task uses a standard text file for storing patient’s username and hashing password for simplicity (see Figure 2), whereas in real-life environment such data would be stored on a database server. To better reflect a real-life scenario, I set up a Mysql server on my Raspberry Pi (see Figure 3). The Queens Medical Centre (queens_mc) database shows a sample of an unhashed  patient registration table consisting of name, password, NHS number, and doctor(specialist).

> joe bloggs , vb123456 
#### Figure 2. A sample of the  patient’s raw data in a text file.  
  
![Mysql table](images/Table.png)
#### Figure 3. A representation of the patient’s raw data in a Mysql database.  



##
##
## References
* Docs.python.org. (2022) Hashlib — Secure hashes and message digests — Python 3.8.4rc1 documentation. Available from: https://docs.python.org/3/library/hashlib.html [Accessed 14 Feb. 2022].
* Fromaget, P. (2022) How to Learn to Program in Python with a Raspberry Pi? Raspberry tips. Available from: https://raspberrytips.com/python-tutorial-raspberry-pi/ [Accessed 22 Jan. 2022].
* GeeksforGeeks (2019). Password validation in Python - GeeksforGeeks. Available from: https://www.geeksforgeeks.org/password-validation-in-python/ [Accessed 9 Feb. 2022].
* Python, R. (2022) Object-Oriented Programming (OOP) in Python 3 – Real Python. realpython.com. Available from: https://realpython.com/python3-object-oriented-programming/ [Accessed 8 Feb. 2022].

