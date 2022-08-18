solution to bash projects exercises

0. Create a SSH RSA key pair

	Read for this task:

[Linux and Mac OS users](https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys)

[Windows users](https://docs.rackspace.com/support/how-to/generating-rsa-keys-with-ssh-puttygen/)

	man: ssh-keygen

You will soon have to manage your own servers concept page hosted on remote [data centers](https://www.youtube.com/watch?v=iuqXFC_qIvA&feature=youtu.be&t=46). We need to set them up with your RSA public key so that you can access them via SSH.

	Create a RSA key pair.
	Requirements:

		Share your public key in your answer file 0-RSA_public_key.pub
		Fill the SSH public key field of your intranet profile with the public key you just generated
		Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
		If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase


1. Write a Bash script that displays Best School 10 times.

	Requirement:
		You must use the for loop (while and until are forbidden)

2. Write a Bash script that displays Best School 10 times.

	Requirement:
		You must use the while loop (for and until are forbidden)

3. Write a Bash script that displays Best School 10 times.

	Requirement:
		You must use the until loop (for and while are forbidden)
