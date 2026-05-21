# Estsolstitiale
<div align="center">

<pre>
                                  @**                           %=@                                 
                                   @@                            @                                  
                                     %%                        %%               :                   
                   @@                  %%                   @%.               @%%                   
                      =                   %               *                 =:                      
                       %%                  %             =                #%                        
                        +* %              %+             *%            =  @                         
                       %%:@*                %           %              *@@@+                        
                        @*@@                =@@=**+**@@=%             @@**@                         
                        @*@@                %@%@%*#%@@%@@              @+@@                         
                        %*%@            =@%@*+*%#**%@@@@*=*@@         *%*@@                         
                        %@*@%           @#@*%#@#*+**%@%@@@@@@         **+%@                         
                        -@*%@            %@@@@***%+*@@@@@@@@          %**@%                         
                          @*@%         *%@@%%*#**++*#%@@@@@@%*        %+@%                          
                           @#%       +%%@@%#**+++*++*%@@@@@@@@%#+     #@                            
                             % %*  @#%%@%+++=*+****+**#@@@@%@@@@#@=%@%@                             
                             @=*@@#+%%%*+++++*+**+****%@@@@@@@@@@*@%*%*                             
                               %%@*#+++**=*+*+*****+**#%@@@@%@@@@@@%                                
                                 =***++*++****+*%******@@@@@@@@@@%%%                                
                                  %++*##*+*+**##******%@@@@@@@@@%@%                                 
                                   =**#%%%%@@@#*****%@@@@@@@@@%@@%                                  
                           @%%@%%%   %  @@%*@%*%@%@@@@%@@@##      @#+%%#%%                          
                       @@*@@@@@@@@*****+=++*%+*%@*%@++=@*@@@@*@@@@%#%#%*%#*@@                       
                   .@#+@@    *%@@%%@@#**#****%#*%@#%*@@@@@@@@@@@@@@=%%#    %@*#%%                   
               =  ***@%          @*@@%%#**#***+*#%**%@@@@@@@@@@@@@@@          @@@@                  
           @%%   % % %          :@@@@@#***#***+*@%**%@@@@@@@@@@@@@@@           * :  @%%+%%          
          .       *             #@%@@******+++*+%%**%@@@@@@@@@@@@@@@                                
                                %@@@@**%*******+%@**%@@@@@#@@@@%@@@%*                               
                                #@@#@****%+**+%*%@**%@@@@@@@@@@@@@@@%                               
                                *@@@@%%@*+**+*%*%@+*%@@@@@%@@@@@@@@@%                               
                                %@@@@%***#****%+%@=*%@@%@@@@@@@@@@@@#                               
                                %@@@@%#*********%@+%@@@@@@@@@@@%@@@@%                               
                                #@%@@#***%****%*%@**%@@%@@@@@@@@@@@#*                               
                                *@%@@%#***#***##@@**%@@@@@@@@@@@@@@%%@%                             
                              #%#%@@@@@**++**@%#@@#**%@@@@@@@%@@%@@*#%%*@                           
                            @@@@*%@@@@***+****%@@@**+#@@@@@@@@@@@@@%@@#**                           
                           %+%@@*%@@@@*%******%#@@#+**@@@%@@@@@@@@@%    %@                          
                           %@   *%@@@@@****+**@@@@+*+@@@@@@@@@@@@@%%    #*%                         
                           *@    *@@@@*%*****#@@@@##*@@@@@@@@@@@@@%%    @*@                         
                          #*@    #@@@@%%%%*+*%%@%@##%@@@@@@@@@@@@@+     @*@#                        
                          @%@+   -*@@@@@%%*%@@@@@@*%%@@@@@@@@@@@@**    *@*@%                        
                          @%%*    *%@@@%@@@@@@@@@@#%#@@@@@@@@%@%##     %@+@#                        
                         @#@@*      %%@@@@@%@@@%@@*@@#@@@@@@@@@*#      @@+@@                        
                        +@*@@#       %#%%@@@%@@@@@@@@@@%@@@@@@#@       *%+@@                        
                         #*%@%         %**%%%%%%%@@%@%%%@%%*#+         %@+@@                        
                         #**@*                +@##*##@                 %@=@#%                       
                         %**@%:                                        #@*@%                        
                         *@@@%                                         %*@ %                        
                        % %@ @                                           %%                         
                         %@*                                             *+@                        
                         =                                                 @                        
                       :*%                                                 %=@                      
                      :@                                                     %@                     
                     :%                                                       #*                    
                      +                                                                             
                               
</pre>

</div>

**Estsolstitiale** is a minimal privacy-oriented encrypted synchronization helper for OneDrive.

It encrypts your local files with [`age`](https://github.com/FiloSottile/age) before they are uploaded to OneDrive, then lets you decrypt them locally when needed. `age` is a simple, modern and secure file encryption tool with small explicit keys and Unix-style composability. 

Estsolstitiale is designed for people who want the convenience of OneDrive synchronization without giving the OneDrive organization tenant readable access to the actual file contents.

---

## Table of Contents
- [What Estsolstitiale Solves](#what-estsolstitiale-solves)
- [Why This Matters](#why-this-matters)
- [The Name](#the-name)
- [Features](#features)
- [Requirements](#requirements)
  - [Required](#required)
  - [Optional for GUI](#optional-for-gui)
- [Installation](#installation)
- [Linux Tutorial](#linux-tutorial)
  - [Debian / Ubuntu / Linux Mint / Pop!_OS](#debian--ubuntu--linux-mint--pop_os)
  - [Fedora](#fedora)
  - [Arch Linux / Manjaro](#arch-linux--manjaro)
- [macOS Tutorial](#macos-tutorial)
- [Windows / WSL Tutorial](#windows--wsl-tutorial)
- [Directory Structure](#directory-structure)
- [First Run](#first-run)
- [Generating an age Key](#generating-an-age-key)
- [Running the Graphical Interface](#running-the-graphical-interface)
- [Running in CLI Mode](#running-in-cli-mode)
- [Direct CLI Commands](#direct-cli-commands)
- [Typical Workflow](#typical-workflow)
- [Recovering Files if the Local Machine Is Lost](#recovering-files-if-the-local-machine-is-lost)
- [Understanding How the Script Works](#understanding-how-the-script-works)
  - [Configuration](#configuration)
  - [Public Key and Private Key](#public-key-and-private-key)
  - [Encryption Flow](#encryption-flow)
  - [Decryption Flow](#decryption-flow)
- [Dry-Run Mode](#dry-run-mode)
- [GUI Mode](#gui-mode)
- [CLI Mode](#cli-mode)
- [Security Model](#security-model)
- [Privacy Limits](#privacy-limits)
- [Important Safety Notes](#important-safety-notes)
- [Recommended OneDrive Configuration](#recommended-onedrive-configuration)
- [Troubleshooting](#troubleshooting)
- [Example](#example)





---

## The Problem

Many schools, universities, companies, and institutions provide Microsoft 365 accounts with OneDrive storage.

This is convenient, but it creates an important privacy issue:

> In an organization-managed OneDrive environment, your files are not protected with personal end-to-end encryption by default.

Microsoft 365 administrators and compliance teams can, depending on permissions and internal policy, search, preserve, export, or access content stored in OneDrive for Business through Microsoft Purview eDiscovery and related administrative tools. Microsoft documentation describes eDiscovery searches across OneDrive and SharePoint sites, including document and file properties. 

Microsoft Q&A also states that an admin can access files stored in OneDrive for Business accounts in an organization in specific situations such as security or compliance investigations, and that the user may not necessarily receive a notification. 

This does not mean that every admin is reading everyone’s files all the time. But it does mean that the organization’s OneDrive is not the same as a private encrypted vault controlled only by you.

For sensitive personal notes, academic documents, research files, administrative documents, private archives, or personal backups, this can be a concern.

---

## What Estsolstitiale Solves

Estsolstitiale solves this problem by changing what OneDrive receives.

Instead of uploading readable files like:

```text
document.pdf
notes.md
archive.zip
VID-2026-21-05.mp4
````

Estsolstitiale uploads encrypted files like:

```text
document.pdf.age
notes.md.age
archive.zip.age
VID-2026-21-05.mp4.age
```

The clear files stay locally in:

```text
~/estsolstitiale/source
```

The encrypted versions are written to:

```text
~/OneDrive/encrypted
```

Then the normal OneDrive Linux client uploads only the encrypted `.age` files.

So the organization sees filenames and folder structure, but not the readable content of the files.

***

## Why This Matters

Without Estsolstitiale:

```text
Your file -> OneDrive cloud -> organization can potentially access content
```

With Estsolstitiale:

```text
Your file -> local encryption -> encrypted .age file -> OneDrive cloud
```

Only the holder of the private age key can decrypt the files. `age` supports encrypting to public recipients and decrypting with an identity/private key file.

This makes OneDrive act more like a transport and storage layer, not a trusted private document vault.

***

## The Name

The name **Estsolstitiale** is inspired by *Amphimallon solstitiale*, also known as the **summer chafer** or **European June beetle**. This beetle belongs to the scarab family and is commonly associated with summer evenings, hedgerows, gardens, and dusk activity.

In short:

> Estsolstitiale protects your files with a shell before they leave your machine.

***

## Features

* encrypt local files before OneDrive upload
* decrypt encrypted files back into a local readable folder
* keep encrypted cloud files synchronized with local source files
* remove orphan encrypted files when source files are deleted
* remove orphan decrypted files when encrypted files are deleted
* dry-run mode to preview actions without modifying files
* first-run setup wizard
* terminal CLI mode
* ultra-lightweight graphical interface
* live logs in the GUI
* atomic writes using temporary files
* maximum file size protection
* no custom database required
* simple folder structure

***

## Requirements

### Required

You need Python 3:

```bash
python3 --version
```

You need `age`:

```bash
age --version
```

You need `age-keygen` if you want automatic public key detection:

```bash
age-keygen --help
```

You need the OneDrive Linux client if you want automatic upload to OneDrive:

```bash
onedrive --version
```

Estsolstitiale uses the `onedrive` Linux client to perform synchronization with Microsoft OneDrive. The abraunegg OneDrive client supports OneDrive Personal, OneDrive for Business, Office 365, SharePoint libraries, and several synchronization modes.

### Optional for GUI

The graphical interface uses Python’s built-in `tkinter`.

Tkinter is the standard Python interface to Tcl/Tk, and Python documentation notes that running `python -m tkinter` should open a small test window when Tkinter is correctly installed.

***

## Installation

Download or clone the project:

```bash
git clone https://github.com/your-user/estsolstitiale.git
cd estsolstitiale
```

Make the script executable:

```bash
chmod +x estsolstitiale.py
```

Run it:

```bash
./estsolstitiale.py
```

or:

```bash
python3 estsolstitiale.py
```

***

## Linux Tutorial

This is the recommended platform because the script currently uses the Linux `onedrive` client.

The abraunegg OneDrive client supports major Linux distributions and OneDrive Personal, OneDrive for Business, Microsoft 365, and SharePoint libraries.

### Debian / Ubuntu / Linux Mint / Pop!\_OS

Install Python, Tkinter, age:

```bash
sudo apt update
sudo apt install python3 python3-tk age
```

Tkinter may need to be installed as `python3-tk` on Ubuntu and Debian-based distributions.

Install the OneDrive client.

For Ubuntu-based distributions, the upstream project recommends using the correct supported packages rather than outdated default repository versions.
Then check:

```bash
python3 --version
age --version
age-keygen --help
onedrive --version
```

Authenticate OneDrive:

```bash
onedrive
```

Follow the login URL shown in the terminal.

Then test synchronization:

```bash
onedrive --synchronize --verbose
```

Run Estsolstitiale:

```bash
python3 estsolstitiale.py
```

***

### Fedora

Install Python, Tkinter, age, and OneDrive:

```bash
sudo dnf install python3 python3-tkinter age onedrive
```

Fedora uses the `python3-tkinter` package name for Tkinter.

Check:

```bash
python3 --version
age --version
onedrive --version
```

Authenticate OneDrive:

```bash
onedrive
```

Run:

```bash
python3 estsolstitiale.py
```

***

### Arch Linux / Manjaro

Install Python, Tkinter, and age:

```bash
sudo pacman -Syu python tk age
```

For the OneDrive client, the upstream installation documentation mentions the Arch User Repository package `onedrive-abraunegg`.

Using an AUR helper such as `yay`:

```bash
yay -S onedrive-abraunegg
```

Check:

```bash
python --version
age --version
onedrive --version
```

Run:

```bash
python estsolstitiale.py
```

***

## macOS Tutorial

macOS can run the GUI and the encryption logic, and `age` is available through Homebrew.

However, the current script expects the Linux `onedrive` command for automatic upload. On macOS, you have two practical options:

1. use Estsolstitiale with `--no-upload`, then sync the encrypted folder manually with the official OneDrive app
2. adapt the `encrypted` path to your local OneDrive folder and avoid calling the Linux `onedrive` client

### Install Homebrew

If Homebrew is not installed, install it from:

```text
https://brew.sh
```

### Install age

```bash
brew install age
```

Homebrew provides an `age` formula for macOS and Linux. [\[deepwiki.com\]](https://deepwiki.com/FiloSottile/age/1.1-installation)

### Check Python and Tkinter

macOS Python builds often include Tkinter, and Python documentation states that `python -m tkinter` can be used to verify Tkinter installation.

Test:

```bash
python3 -m tkinter
```

If a small window appears, Tkinter works.

### Run Estsolstitiale

```bash
python3 estsolstitiale.py gui
```

### Encrypt without Linux OneDrive upload

```bash
python3 estsolstitiale.py encrypt --no-upload
```

Then make sure your encrypted folder is inside your OneDrive-synced directory, or manually move/sync the encrypted `.age` files.

***

## Windows / WSL Tutorial

The recommended Windows setup is **WSL2**, because Estsolstitiale currently expects Linux-style paths and the Linux `onedrive` client.

`age` itself is cross-platform and can be installed on Windows through package managers such as Chocolatey or Scoop according to installation references.

But for the full Estsolstitiale workflow with the `onedrive` CLI, use WSL.

### Step 1: Install WSL2

Open PowerShell as Administrator:

```powershell
wsl --install
```

Restart if required.

Install Ubuntu from the Microsoft Store if it was not installed automatically.

Open Ubuntu.

### Step 2: Install dependencies inside WSL

Inside Ubuntu/WSL:

```bash
sudo apt update
sudo apt install python3 python3-tk age
```

Install the supported OneDrive Linux client following the upstream client documentation. The upstream documentation recommends supported packages for Debian/Ubuntu-based distributions rather than outdated default repository versions.

### Step 3: Authenticate OneDrive

Inside WSL:

```bash
onedrive
```

Follow the login URL.

Then test:

```bash
onedrive --synchronize --verbose
```

### Step 4: Run Estsolstitiale

```bash
python3 estsolstitiale.py
```

### Important note for Windows users

The official Windows OneDrive client and the Linux `onedrive` CLI are different tools.

If you want to use the native Windows OneDrive app instead of the Linux CLI, you should run:

```bash
python3 estsolstitiale.py encrypt --no-upload
```

Then make sure the encrypted output folder is placed inside a Windows OneDrive-synced directory.

***

## Directory Structure

Estsolstitiale uses this local structure:

```text
~/estsolstitiale/
├── source/
├── decrypted/
└── config/
    ├── public_key.txt
    └── age_key.txt
```

And this OneDrive-side folder:

```text
~/OneDrive/encrypted/
```

### Meaning of each folder

```text
~/estsolstitiale/source
```

This is where you put the original readable files.

```text
~/OneDrive/encrypted
```

This is where Estsolstitiale writes encrypted `.age` files.

```text
~/estsolstitiale/decrypted
```

This is where decrypted files are restored when you run decrypt.

```text
~/estsolstitiale/config
```

This stores the age public key and copied private key.

***

## First Run

By default, running the script without arguments starts the graphical interface:

```bash
python3 estsolstitiale.py
```

If no configuration exists yet, click:

```text
Setup
```

The setup asks for:

* your age private key
* your age public key

If `age-keygen` is installed, Estsolstitiale can detect the public key from the private key automatically.

You can also run setup from the terminal:

```bash
python3 estsolstitiale.py setup
```

To force setup again:

```bash
python3 estsolstitiale.py setup --force
```

To delete the configuration:

```bash
python3 estsolstitiale.py reset-config
```

***

## Generating an age Key

If you do not already have an age key:

```bash
mkdir -p ~/.config/age
age-keygen -o ~/.config/age/key.txt
```

This prints a public key like:

```text
Public key: age1...
```

Your private key is stored in:

```text
~/.config/age/key.txt
```

During Estsolstitiale setup, provide that private key path.

The public key can be extracted later with:

```bash
age-keygen -y ~/.config/age/key.txt
```

The `age-keygen -y` workflow converts an identity/private key into the matching recipient/public key.

***

## Running the Graphical Interface

Start the GUI:

```bash
python3 estsolstitiale.py
```

or:

```bash
python3 estsolstitiale.py gui
```

The GUI provides:

* `Encrypt + Sync`
* `Decrypt`
* `Dry Encrypt`
* `Dry Decrypt`
* `Setup`
* `Open Source`
* `Open Encrypted`
* `Open Decrypted`
* live logs at the bottom

The GUI is intentionally minimal. It only wraps the same operations as the CLI.

***

## Running in CLI Mode

To launch the terminal menu exactly like the classic script:

```bash
python3 estsolstitiale.py cli
```

You can also use:

```bash
python3 estsolstitiale.py menu
```

The menu provides:

```text
1. Encrypt, sync and upload
2. Sync and decrypt
3. Dry-run encrypt
4. Dry-run decrypt
5. Reconfigure
6. Exit
```

***

## Direct CLI Commands

Encrypt and upload:

```bash
python3 estsolstitiale.py encrypt
```

Encrypt without uploading:

```bash
python3 estsolstitiale.py encrypt --no-upload
```

Preview encryption without modifying files:

```bash
python3 estsolstitiale.py encrypt --dry-run --no-upload
```

Decrypt:

```bash
python3 estsolstitiale.py decrypt
```

Preview decryption:

```bash
python3 estsolstitiale.py decrypt --dry-run
```

Verbose logs:

```bash
python3 estsolstitiale.py encrypt --verbose
```

Setup:

```bash
python3 estsolstitiale.py setup
```

Force setup:

```bash
python3 estsolstitiale.py setup --force
```

Reset configuration:

```bash
python3 estsolstitiale.py reset-config
```

***

## Typical Workflow

Put your readable files here:

```text
~/estsolstitiale/source
```

Example:

```text
~/estsolstitiale/source/
├── history/
│   └── course.pdf
├── notes/
│   └── private_notes.md
└── archive.zip
```

Run:

```bash
python3 estsolstitiale.py encrypt
```

Estsolstitiale creates:

```text
~/OneDrive/encrypted/
├── history/
│   └── course.pdf.age
├── notes/
│   └── private_notes.md.age
└── archive.zip.age
```

Then it runs:

```bash
onedrive --synchronize --verbose
```

The OneDrive client uploads the encrypted `.age` files.

To restore readable files later:

```bash
python3 estsolstitiale.py decrypt
```

This creates:

```text
~/estsolstitiale/decrypted/
├── history/
│   └── course.pdf
├── notes/
│   └── private_notes.md
└── archive.zip
```

***

## Recovering Files if the Local Machine Is Lost

This is one of the most important parts of using Estsolstitiale.

If your computer is lost, broken, stolen, erased, or reinstalled, your readable local files in:

```text
~/estsolstitiale/source
```

may be gone.

But if synchronization succeeded, your encrypted files should still exist online in OneDrive:

```text
encrypted/*.age
```

You can recover them **only if you still have your age private key**.

### Absolute rule

> If you lose the private key, you lose the ability to decrypt the files.

The encrypted `.age` files stored online are intentionally unreadable without the private key. This is the point of the tool.

Therefore, you must back up this file:

```text
~/estsolstitiale/config/age_key.txt
```

or the original age key, for example:

```text
~/.config/age/key.txt
```

### Recommended private key backups

Store at least one backup of the private key in a secure place, for example:

* an encrypted USB drive
* an offline external drive
* a password manager that supports secure file attachments
* a printed paper backup stored safely
* a separate encrypted backup system

Do **not** store the private key in the same OneDrive folder as your encrypted files.

Do **not** put the private key in:

```text
~/estsolstitiale/source
```

Do **not** put the private key in:

```text
~/OneDrive/encrypted
```

If you upload the private key next to the encrypted files, you destroy the security model.

***

### Recovery Scenario

Assume your old computer is gone.

You still have:

* access to your OneDrive account
* the encrypted `.age` files online
* a backup of your private key

You can recover your files like this.

***

### Step 1: Install Estsolstitiale on the new machine

Clone or copy the script again:

```bash
git clone https://github.com/your-user/estsolstitiale.git
cd estsolstitiale
```

or manually copy:

```text
estsolstitiale.py
```

***

### Step 2: Install dependencies

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-tk age
```

Install and configure the OneDrive Linux client as described above.

***

### Step 3: Restore your private key

Create the config folder:

```bash
mkdir -p ~/estsolstitiale/config
```

Copy your backed-up private key:

```bash
cp /path/to/your/backup/age_key.txt ~/estsolstitiale/config/age_key.txt
chmod 600 ~/estsolstitiale/config/age_key.txt
```

***

### Step 4: Recreate the public key file

Generate the public key from the private key:

```bash
age-keygen -y ~/estsolstitiale/config/age_key.txt > ~/estsolstitiale/config/public_key.txt
```

Check it:

```bash
cat ~/estsolstitiale/config/public_key.txt
```

It should start with:

```text
age1
```

***

### Step 5: Download encrypted files from OneDrive

If you use the Linux OneDrive client:

```bash
onedrive --synchronize --verbose
```

Make sure the encrypted files are present in:

```text
~/OneDrive/encrypted
```

You should see files like:

```text
document.pdf.age
notes.md.age
archive.zip.age
```

***

### Step 6: Decrypt

Run:

```bash
python3 estsolstitiale.py decrypt
```

Your recovered readable files should appear in:

```text
~/estsolstitiale/decrypted
```

***

### Step 7: Optional: restore them as source files

If you want to continue using Estsolstitiale normally, you can copy the recovered files back into:

```text
~/estsolstitiale/source
```

Example:

```bash
cp -a ~/estsolstitiale/decrypted/. ~/estsolstitiale/source/
```

Then future encryptions will work again.

***

## Understanding How the Script Works

This section explains the internal logic precisely.

***

### Configuration

The script defines a `Config` object containing:

```python
base
source
encrypted
decrypted
config_dir
public_key_file
private_key_file
public_key
```

The default paths are:

```python
base = ~/estsolstitiale
source = ~/estsolstitiale/source
encrypted = ~/OneDrive/encrypted
decrypted = ~/estsolstitiale/decrypted
config_dir = ~/estsolstitiale/config
public_key_file = ~/estsolstitiale/config/public_key.txt
private_key_file = ~/estsolstitiale/config/age_key.txt
```

The setup step creates these directories and stores:

```text
public_key.txt
age_key.txt
```

The private key is copied into the config directory and its permissions are restricted to `600` when possible.

***

### Public Key and Private Key

The public key is used to encrypt files.

The private key is used to decrypt files.

Encryption uses:

```bash
age -r PUBLIC_KEY -o output.age input
```

Decryption uses:

```bash
age -d -i age_key.txt -o output input.age
```

This matches the normal age model: encryption uses recipient public keys, and decryption uses identity/private key files.

***

### Encryption Flow

When you run:

```bash
python3 estsolstitiale.py encrypt
```

the script does this:

1. loads the configuration
2. checks that `age` exists
3. checks that `onedrive` exists unless `--no-upload` is used
4. scans all files in:

```text
~/estsolstitiale/source
```

5. ignores files larger than `MAX_SIZE`

```python
MAX_SIZE = 10 * 1024 * 1024 * 1024
```

That means 10 GB.

6. for each source file, computes the matching encrypted path

Example:

```text
~/estsolstitiale/source/folder/file.pdf
```

becomes:

```text
~/OneDrive/encrypted/folder/file.pdf.age
```

7. checks whether the encrypted file should be updated

A file is encrypted if:

* the `.age` file does not exist
* or the source file is newer than the encrypted file

8. writes encryption output to a temporary file first

Example:

```text
file.pdf.age.tmp
```

9. if encryption succeeds, replaces the final `.age` file atomically

This avoids leaving broken encrypted files if encryption fails halfway.

10. removes encrypted files that no longer have a matching source file

Example:

```text
~/OneDrive/encrypted/old.pdf.age
```

is removed if:

```text
~/estsolstitiale/source/old.pdf
```

does not exist.

11. removes empty directories

12. optionally runs OneDrive upload:

```bash
onedrive --synchronize --verbose
```

***

### Decryption Flow

When you run:

```bash
python3 estsolstitiale.py decrypt
```

the script does this:

1. loads the configuration
2. checks that `age` exists
3. scans all `.age` files in:

```text
~/OneDrive/encrypted
```

4. computes the matching decrypted path

Example:

```text
~/OneDrive/encrypted/folder/file.pdf.age
```

becomes:

```text
~/estsolstitiale/decrypted/folder/file.pdf
```

5. skips files that are already up to date

A file is decrypted if:

* the decrypted file does not exist
* or the encrypted file is newer than the decrypted file

6. writes decrypted output to a temporary file first

Example:

```text
file.pdf.tmp
```

7. if decryption succeeds, replaces the final decrypted file

8. removes decrypted files that no longer have a matching encrypted `.age` file

9. removes empty directories

***

### Dry-Run Mode

Dry-run means:

> show what would happen, but do not modify anything.

Example:

```bash
python3 estsolstitiale.py encrypt --dry-run --no-upload
```

In dry-run mode, the script does not:

* encrypt files
* decrypt files
* delete orphan files
* remove directories
* upload to OneDrive

It only logs the actions it would perform.

This is useful before a first real run or before deleting/moving many files.

***

### GUI Mode

The GUI uses `tkinter`.

It does not implement different logic. It calls the same Python functions as the CLI:

```python
encrypt_sync()
decrypt_sync()
first_setup()
load_config()
ensure_directories()
```

Long tasks run in a background thread so the interface does not freeze.

Logs are redirected to a queue and displayed in the log area at the bottom of the window.

***

### CLI Mode

The CLI mode uses `argparse`.

The command is parsed here:

```python
parse_args()
```

Then routed through:

```python
run_cli()
```

If the command is:

```text
cli
```

or:

```text
menu
```

the script opens the interactive terminal menu.

If the command is:

```text
encrypt
decrypt
setup
reset-config
```

the script runs that action directly.

***

## Security Model

Estsolstitiale protects **file contents** before they reach OneDrive.

It does not hide everything.

### Protected

The following are encrypted:

* document contents
* PDF contents
* text contents
* images
* archives
* any file payload

### Not Fully Protected

The following may still be visible to OneDrive or the organization:

* filenames
* folder names
* file sizes
* modification times
* number of files
* upload times
* account metadata

Example:

```text
Medical_Report.pdf.age
```

still reveals that a file probably relates to a medical report.

If that matters, rename files before encryption:

```text
001.age
002.age
003.age
```

or store files inside an encrypted archive before putting them in `source`.

***

## Privacy Limits

Estsolstitiale is not magic.

It does not:

* make OneDrive anonymous
* hide that you uploaded encrypted files
* hide your account identity
* hide file sizes
* hide folder structure
* protect files already uploaded unencrypted before using the tool
* replace a full encrypted filesystem
* replace operational security

It does one thing well:

> It prevents OneDrive from receiving readable file contents.

***

## Important Safety Notes

Keep your private key safe.

If you lose:

```text
~/estsolstitiale/config/age_key.txt
```

and you have no backup, you may lose access to your encrypted files.

Back it up offline, for example:

```bash
cp ~/estsolstitiale/config/age_key.txt ~/secure-backup/age_key.txt
```

Do not upload your private key to OneDrive.

Do not put the private key inside:

```text
~/estsolstitiale/source
```

Do not put the private key inside:

```text
~/OneDrive/encrypted
```

The private key is the only thing that lets you recover your files from the encrypted online copies.

***

## Recommended OneDrive Configuration

If you see errors like:

```text
Stream error in the HTTP/2 framing layer
```

during upload, this is usually an issue with the OneDrive Linux client, HTTP/2, curl, or the network path.

A known workaround is to force HTTP/1.1 in the OneDrive client configuration:

```ini
force_http_11 = "true"
```

Edit:

```bash
nano ~/.config/onedrive/config
```

Add:

```ini
force_http_11 = "true"
```

Then run:

```bash
onedrive --synchronize --verbose
```

***

## Troubleshooting

### `Command not found: age`

Install age.

Debian / Ubuntu:

```bash
sudo apt install age
```

Arch:

```bash
sudo pacman -S age
```

Fedora:

```bash
sudo dnf install age
```

`age` is available through multiple operating system package managers, including apt, pacman, dnf, Homebrew, Chocolatey, and Scoop.

***

### `Command not found: onedrive`

Install the OneDrive Linux client.

Then authenticate it:

```bash
onedrive
```

Follow the browser login instructions.

After authentication, test:

```bash
onedrive --synchronize --verbose
```

***

### GUI does not start

Install Tkinter.

Debian / Ubuntu:

```bash
sudo apt install python3-tk
```

Fedora:

```bash
sudo dnf install python3-tkinter
```

Arch:

```bash
sudo pacman -S tk
```

Then retry:

```bash
python3 estsolstitiale.py gui
```

Tkinter can be tested with:

```bash
python3 -m tkinter
```

Python documentation says this command should open a small window when Tkinter is installed correctly.

***

### Configuration not found

Run:

```bash
python3 estsolstitiale.py setup
```

or open the GUI and click:

```text
Setup
```

***

### Public key invalid

A valid age public key usually starts with:

```text
age1
```

Example:

```text
age1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

You can derive it from your private key:

```bash
age-keygen -y ~/.config/age/key.txt
```

***

### Private key invalid

A valid age private key file contains a line starting with:

```text
AGE-SECRET-KEY-
```

If your file does not contain that, it is probably not an age private key.

***

### Files are not uploaded

First encrypt without upload:

```bash
python3 estsolstitiale.py encrypt --no-upload
```

Then check:

```text
~/OneDrive/encrypted
```

If `.age` files exist there, Estsolstitiale worked.

Then test OneDrive manually:

```bash
onedrive --synchronize --verbose
```

If that fails, the issue is likely with the OneDrive client configuration, not Estsolstitiale.

***

## Example

Create a test file:

```bash
mkdir -p ~/estsolstitiale/source
echo "private note" > ~/estsolstitiale/source/note.txt
```

Encrypt:

```bash
python3 estsolstitiale.py encrypt --no-upload
```

You should see:

```text
~/OneDrive/encrypted/note.txt.age
```

Decrypt:

```bash
python3 estsolstitiale.py decrypt
```

You should see:

```text
~/estsolstitiale/decrypted/note.txt
```

Check content:

```bash
cat ~/estsolstitiale/decrypted/note.txt
```

Expected:

```text
private note
```

***
