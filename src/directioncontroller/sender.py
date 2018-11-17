import argparse

known_directions = ['start', 'stop', 'left', 'right', 'forward', 'back']



class Direction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        direction = values[0]
        if direction.lower() not in known_directions:
            parser.error("Unknown direction. Available direction are 'start', 'stop', 'left', 'right', 'forward', & 'back'")
        namespace.direction = direction.lower()



def create_parser():
    parser = argparse.ArgumentParser(description="""
    Control the movement of your bot.
    """)
    parser.add_argument('--direction', '-d',
                        help='which direction to move',
                        nargs=1,
                        metavar=("DIRECTION"),
                        action=Direction,
                        required=True)
    return parser

def main():
    from directioncontroller import controller, client

    args = create_parser().parse_args()
    client.client_socket()
    controller.json_message(args.direction)
    print("Sending direction %s" % args.direction )



