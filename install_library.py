import subprocess
import sys
import pkg_resources

def packages_control():
    packages = ["numpy", "pandas", "seaborn", "nltk"]
    not_install_packages = []
    add_package_question = input("Do you want to add library ? Please enter YES or NO ! ").upper()
    if add_package_question == "YES":
        add_package_name = input(" Enter the library that needs to be import..." + "\n")
        if add_package_name.isspace():
            print("You cannot enter spaces !")
        elif add_package_name not in packages:
            packages.append(add_package_name)
        for package in packages:
            try:
                dist = pkg_resources.get_distribution(package)
                if dist.key == add_package_name:
                    print("\n", add_package_name + ", library already installed...", "\n")
            except pkg_resources.DistributionNotFound:
                if True:
                    print('{} is NOT installed'.format(package), "\n")
                    not_install_packages.append(package)
                    value = input(package + " Download the package ?").upper()
                    if value == "YES":
                        for package in not_install_packages:
                            try:
                                subprocess.check_call([sys.executable, "-m", "pip", "install", package],
                                                      stderr=subprocess.STDOUT)
                                not_install_packages.remove(package)
                            except subprocess.CalledProcessError as ex:
                                print(package, "library not found ! You may have entered the wrong library name.", "\n")
                                packages.remove(package)
                                continue
                        if not_install_packages == []:
                            print("Successfully installed all packages...", "\n")
                        else:
                            for package in not_install_packages:
                                print(package + ",", "--> the package could not be installed !!!")
    else:
        print("You indicated that you do not want to install a library...", "\n")
    return(dist.key, dist.version)

packages_control()

