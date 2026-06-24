def calculate_download_time():
    print("=======================Download data with mbps==============")
    print("===============This created by Abhishek_mishra==============\n")

    size_gb = float(input("[+]E  Enter file size (GB): "))
    speed_mbps = float(input("[+]  Enter Your wifi speed (Mbps):"))

    size_mb = size_gb * 1024
    speed_mbs = speed_mbps / 8

    total_seconds = size_mb / speed_mbs
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    # ------------output------------------

    print(f"""

    =============================================================
    ||
    ||     File size    :  {size_gb} GB ({size_mb:.0f} MB)
    ||     Speed        :  {speed_mbps} Mbps ({speed_mbs:.2f} MB/s)
    ||     Download time:  {hours} H {minutes} m {seconds} s
    ||
    ==============================================================
""")
calculate_download_time()