import argparse

known_direction = ['start', 'stop', 'left', 'right', 'forward', 'back']


# HOST = '127.0.0.1'
# PORT = 65432


class Direction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        direction = values
        if direction.lower() not in known_direction:
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

parser = create_parser()
parser.parse_args()
# def main():
#     args = create_parser().parse_args()


