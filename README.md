# Gazilion the Brute

## Overview
Gazilion the Brute is a Python tool designed for brute forcing endpoints using a wordlist. It provides a simple yet effective way to perform brute-force attacks on specified target.

## Features
- Customizable wordlists for testing.
- Support for different request methods (get, post).
- Option to specify the target URL and protocol.
- Hide response status code for cleaner output.
- Help option for quick reference to available commands.

## Getting Started

### Prerequisites
- Python3
- pip3

### Screen Shots 📸 :
<h1 align="center">
  <h2 align="center">Screen Shot 1</h2>
  <h1 align="center"><img align="center" src="https://ik.imagekit.io/d3kzbpbila/thejashari_VjvQMlJ2D" width="700px" alt="screenshot1"></h1>
  <h2 align="center">Screen Shot 2</h2>
 <h1 align="center"> <img align="center" src="https://ik.imagekit.io/d3kzbpbila/thejashari_aPZtqin6I5" width="700px" alt="screenshot2"></h1>
 <h2 align="center">Screen Shot 3</h2>
 <h1 align="center"> <img align="center" src="https://ik.imagekit.io/d3kzbpbila/thejashari_iMXhk8HL1" width="700px" alt="screenshot3"></h1>

### Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```
    
2. **Install dependencies (if any):**
    ```bash
    pip install -r requirements.txt
    ```
### Making the Tool Global

To make Gazilion the Brute globally accessible from any directory, follow these steps:

1. Open your Zsh configuration file (`~/.zshrc`) in a text editor:
    ```bash
    nano ~/.zshrc
    ```
    Replace `nano` with your preferred text editor.

2. Add the following line at the end of the file, replacing `/path/to/tool/directory` with the actual path to the tool directory:
    ```bash
    export PATH=$PATH:/path/to/tool/directory
    ```

3. Save the file and exit the text editor.

4. Reload your Zsh configuration to apply the changes:
    ```bash
    source ~/.zshrc
    ```

Now, you can run Gazilion the Brute from any directory using:
```bash
python3 brute.py
```

### Usage

#### Options
- **-m <method>:** Method of the request ['get', 'post']
- **-t <target>:** Target URL
- **-p <protocol>:** Protocol options are ['http', 'https']
- **-hR:** Hide response status code
- **-w <wordlist>:** Path to the wordlist file (default: default_wordlist.txt)
- **-h:** Help

#### Example
Run the tool with the following command:
```bash
python3 brute.py -t 'https://your-target.com' -m post -p https -hR 500,404 -w custom_wordlist.txt
```

### Connect with me on
<a href="https://www.linkedin.com/in/thejashari/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="cyberspartan" height="30" width="40" /></a>
<a href="https://instagram.com/nuthejashari" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="karthithehacker" height="30" width="40" /></a>
