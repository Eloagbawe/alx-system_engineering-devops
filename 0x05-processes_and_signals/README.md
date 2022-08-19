solution to bash scripting exercises

0. Write a Bash script that displays its own PID.

1. Write a Bash script that displays a list of currently running processes.

	Requirements:
		Must show all processes, for all users, including those which might not have a TTY
		Display in a user-oriented format
		Show process hierarchy

2. Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

	Requirements:

	You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))