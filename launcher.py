import sys
import subprocess
import importlib.util
import os

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
        # Look for any file starting with 'main' and ending with '.pyc'
        pyc_files = [f for f in os.listdir('.') if f.startswith('main') and f.endswith('.pyc')]
        if not pyc_files:
            raise ImportError("No main.pyc file found")
            
        # Use the first matching file
        spec = importlib.util.spec_from_file_location("main", pyc_files[0])
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        scanner = module.ArkAnalyzer()
        scanner.run()
    except Exception as e:
        print("Error: Make sure launcher.py and the main.pyc file are in the same directory")
        print(f"Details: {str(e)}")

if __name__ == "__main__":
    main()