# IAM Manager

> 🧑‍🔬 Manage your AWS IAM users easily and efficiently 

<br>
<br>

### Features

#### IAM
- [x] : List IAM Users

#### MFA
- [x] : Get IAM Users with no MFA enabled
- [x] : Save no MFA user list to either `.txt` or `.csv` file


<br>
<br>

### How to run

#### 1. Create a virtual environment called venv
```bash
python3 -m venv venv
```
<br>

#### 2. Activate your virtual environment

```
source venv/bin/activate
```
<br>

#### 3. Install the required packages
```bash
python3 -m pip install --upgrade pip # upgrade your pip
pip3 install -r requirements.txt
```

<br>

#### 4. Modify configs

In `src/configs/configs.py`, you'll see some variables in there.
Make changes to them as desired.

##### Variables
- NO_MFA_USER_FILE
  - Name of the file to save no MFA user list
- FILE_PATH
  - Literally file path

<br>

#### 5. Now, run!

```bash
cd src
python3 main.py 
```