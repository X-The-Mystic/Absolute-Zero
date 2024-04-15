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

        self.target_text = tk.Text(self.root, height=5, width=30)
        self.ping_number = tk.Entry(self.root)
        self.target_port = tk.Entry(self.root)
        self.packet_size = tk.Entry(self.root)
        self.attack_duration = tk.Entry(self.root)
        self.attack_vector_entry = tk.StringVar
        self.attack_vector_entry.set("ICMP echo")

        self.attack_vectors = [
            "ICMP echo", "ICMP burst", "PoD Attack"
        ]

        self.attack_num = 0
        self.stop_attack_flag = False
        self.target_status = Active
        self.total_bytes_sent = 0

        self.create_gui()

    def create_gui(self)
        tk.Label(self.root, text="Enter the target's IPv4 address or the website domain name (one per line)").pack()
        self.target_text.pack()























