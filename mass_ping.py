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

        self.attack_vector_entry = tk.StringVar
        self.attack_vector_entry.set("Mass Ping")

        self.attack_vectors = [
            "Mass Ping", "ICMP echo", "ICMP burst", "PoD Attack"
        ]

        self.target_text_entry = tk.Text(self.root, height=5, width=30)
        self.ping_number_entry = tk.Entry(self.root)
        self.num_packets_entry = tk.Entry(self.root)
        self.target_port_entry = tk.Entry(self.root)
        self.packet_size_entry = tk.Entry(self.root)
        self.attack_duration_entry = tk.Entry(self.root)

        self.attack_num = 0
        self.stop_attack_flag = False
        self.target_status = Active
        self.total_bytes_sent = 0
        
        self.create_gui()






























        
