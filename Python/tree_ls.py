from os import path as os_path, listdir
import argparse

"""
Fast, simple just for fun tree like file listing
Usage: python3 tree_ls.py /directory
"""

# Global variables
BLUE = "\033[1;36;40m"
RESET_COLOR = "\033[0m"
VERTICAL = "|"
T1 = "└"

def tree(path, items=[], depth=1):
    # depth first search
    if not items:
        try:
            items = listdir(path)
        except PermissionError:
            print(f"Error opening dir {path}")
        except Exception as e:
            print(e)
    MAKE_SPACE = " " * depth
    while items:
        current = items.pop()
        if os_path.isdir(f"{path}{current}"):
            print(f"{MAKE_SPACE}{T1}", end="")
            try:
                next_items = listdir(f"{path}{current}/")
            except PermissionError:
                print(f"{BLUE}{current}{RESET_COLOR} [Error opening dir]")
                continue
            except Exception as e:
                print(e)
            print(f"{BLUE}{current}{RESET_COLOR}")
            tree(path=f"{path}{current}/", items=next_items, depth=depth+4)
        else:
            print(f"{MAKE_SPACE}{T1}", end="")
            print(f"{current}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Directory in which files will be listed in a tree manner")

    global args
    args = parser.parse_args()
    if not args.path.endswith("/"):
        args.path += "/"
    print(f" {BLUE}{args.path}{RESET_COLOR}")
    tree(args.path)


if __name__ == "__main__":
    main()
