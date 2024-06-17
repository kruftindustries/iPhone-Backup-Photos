# iPhone Photo Backup Utility (Windows, Python)
Are you a Windows PC user trying to back up the pictures and videos on your camera roll? Do you prefer the convenience and speed of USC-C file transfer instead of a cloud service? Trying to avoid using a paid app?


This simple python utility will process your iPhone backup SQLite manifest and directory of seemingly random folders and files to produce a single folder with all your pictures and videos!


This requires you make a backup using the Apple Devices program with backup encryption disabled.
<img src="https://github.com/kruftindustries/iPhone-Backup-Photos/assets/22876292/72caa58b-17ff-4807-a2b2-4ab54f9cf480" alt="Apple Devices Backup Settings">

After setting up local backups to "this computer", un-checking "Encrypt local backup" and confirming the changes, click Backup Now

<img src="https://github.com/kruftindustries/iPhone-Backup-Photos/assets/22876292/eaf49786-64c2-4159-8c2c-8ffb6e1035a2" alt="Backup Now">

Once the backup is complete, click "Manage Backups..." select and right click the backup you just took in the list and click "Show in Explorer"

<img src="https://github.com/kruftindustries/iPhone-Backup-Photos/assets/22876292/cc9ef64c-932a-4edb-af83-ec1815ff2d5c" alt="Show in Explorer">

This will open a window of the backup directory. It should be "C:\Users\USER\Apple\MobileSync\Backup\XXXX-XXXXXXXXX".
Copy this path from the address bar and then run/double click the python script. 
A file prompt will pop up asking where the Manifest file is. Paste the path you copied into the address bar, navigate to the path and select the "Manifest.db"

<img src="https://github.com/kruftindustries/iPhone-Backup-Photos/assets/22876292/0d5d001e-afd6-47f9-a8df-8c96c51150c5" alt="Select the Manifest.db file in the backup directory">

Click Open and after some time (30 seconds for a large backup on a fast computer) a GUI displays the files found in a table

<img src="[https://github.com/kruftindustries/iPhone-Backup-Photos/assets/22876292/4f4274b9-cca8-4bc8-b9b4-327b49d0fd86](https://github.com/kruftindustries/iPhone-Backup-Photos/assets/22876292/fd61556c-6b27-4ce3-b069-eedcb5043c13)" alt="Select the Manifest.db file in the backup directory">

Click "Process Files" at the bottom and after a few minutes (the GUI might appear to be not responding while this happens, give it a moment) a new folder called "DCIM" containing the recovered files will be added to the backup directory!

<img src="https://github.com/kruftindustries/iPhone-Backup-Photos/assets/22876292/8ad5ba68-f193-43e0-8e8e-afdb2c291cff" alt="Select the Manifest.db file in the backup directory">

Tip: To find the folder more easily, sort by "Date Modified" in file explorer to bring the DCIM folder to the bottom/top

<img src="https://github.com/kruftindustries/iPhone-Backup-Photos/assets/22876292/dde23c7e-b757-4c50-8023-7b2dfc2819ff" alt="Select the Manifest.db file in the backup directory">


Good Luck!
