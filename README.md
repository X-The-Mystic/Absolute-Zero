# Absolute-Zero
This is a specialized type of flood attack, with inspiration taken from JJ email spam. This code pings numerous IPv4 addresses over a broadcast network, then sends the response packets to a target.

# How to Use
Open a terminal and type
`git clone https://github.com/X-The-Mystic/Absolute-Zero`.
Then, type 
`cd Absolute-Zero`.
Finally, to run the code, type 
`python3 main.py`.

# Some Tips:
Before launching the attack, use the command 
`nmap -Pn (port no.) (IPv4 address)`
to ensure that the IPv4 address you are attacking is valid.

While attack is in progress, use a tool such as Wireshark to view the ICMP echo requests, and to see the impact on your computer, use a tool such as Task Manager.

This code was made for educational and pentesting purposes only. I am not responsible for any illegal or irresponsible uses of this code.
