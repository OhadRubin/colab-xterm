import colabxterm
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='python -m colabxterm')
    parser.add_argument("-p", "--port", type=int,
                        help="port number", default=10000)
    parser.add_argument("command", help="Commands to run", nargs='*')
    
    # If there are arguments that look like they belong to a subcommand
    # (like 'echo hello'), pass them through directly
    argv = sys.argv[1:]
    if "--" in argv:
        split_idx = argv.index("--")
        parser_args = argv[:split_idx]
        command_args = argv[split_idx+1:]
        args = parser.parse_args(parser_args)
        args.command = command_args
    else:
        args = parser.parse_args()
    
    port = args.port
    command = args.command
    
    # Debug output to see what command is being passed
    if command:
        print(f"Starting terminal with command: {' '.join(command)}")
    
    term = colabxterm.XTerm(command, port)
    term.open()
