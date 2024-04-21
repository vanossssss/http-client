from http_client import Client
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='enter link and type of request')
    parser.add_argument('link', type=str,
                        help='link to send requests')
    parser.add_argument('request', type=str,
                        help='type of request')
    parser.add_argument('--save', '-s', action='store_true',
                        help='enter key to save response')

    args = parser.parse_args()
    client = Client(args.link)
    if args.request == 'get':
        client.get()
    elif args.request == 'head':
        client.head()
    elif args.request == 'post':
        client.post()

    if args.save:
        client.save_output()
