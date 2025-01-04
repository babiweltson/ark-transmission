import sys
import subprocess

def check_python_version():
    if sys.version_info[0] != 3:
        print("This program requires Python 3")
        sys.exit(1)

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        print(f"Failed to install {package}. Please install it manually using:")
        print(f"pip install {package}")
        sys.exit(1)

def main():
    check_python_version()
    
    # Check and install required package
    try:
        import colorama
    except ImportError:
        print("Installing required package...")
        install_package('colorama')
    
    try:
        from main import ArkAnalyzer
        scanner = ArkAnalyzer()
        scanner.run()
    except Exception as e:
        print("Error: Make sure launcher.py and main.pyc are in the same directory")
        print(f"Details: {str(e)}")

if __name__ == "__main__":
    main()