import argparse

from reviewers import get_git_branches, get_reviewers


parser = argparse.ArgumentParser(description="Get the suggested reviewers for a commit")
parser.add_argument('--branch', '-b',
                    required=False,
                    help="Check for a PR against a specific branch")
parser.add_argument('--contributor', '-c',
                    required=False,
                    help="View lines of code for a specific contributor")
parser.add_argument('files', metavar='file', type=str, nargs='*',
                    help='Only show reviewers for certain files. If none specified, shows reviewers for all files')
args = parser.parse_args()


if args.branch:
    branch = args.branch
elif 'develop' in get_git_branches():
    branch = 'develop'
else:
    branch = 'master'


get_reviewers(args.contributor, branch, args.files)