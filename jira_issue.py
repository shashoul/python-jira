from jira import JIRA
from datetime import datetime
import argparse

In_Progress = '31'


def jira_issue(args):
    """
    jira_issue: create a jira issue.
    """
    try:
        jira = JIRA('https://clewmed.atlassian.net',basic_auth=(args.USERNAME, args.TOKEN))

        issue_text = f'{args.JOBNAME} {datetime.now().strftime("%m/%d/%Y, %H:%M")}'

        issue_fields ={
            'project': {'key': 'CLEWOPS'},
            'summary': issue_text,
            'description': issue_text,
            'issuetype': {'name': 'Story'},
            'assignee' : { 'accountId' : '5c77b1e2a5f3422150243a64' }
        }

        issueTiket = jira.create_issue(fields=issue_fields)
        print("Jira Issue tiket has been created " + issueTiket.key)

        # move ticket to in progress status.
        jira.transition_issue(issueTiket,In_Progress)

    except Exception as e:
        print(e)
    

def get_arguments():
    """
    get_arguments: get command line arguments.

    """
    parser = argparse.ArgumentParser(description='JIRA Issue creator')
    parser.add_argument('--USERNAME', required=True, help='username to authenticate with jira')
    parser.add_argument('--TOKEN', required=True, help="token to authinticate with jira")
    parser.add_argument('--JOBNAME', required=False, help='JENKINS job name that triggered the jira issue creator ')

    parser.set_defaults(release=True)
    return parser.parse_args()


def main():
    args = get_arguments()
    jira_issue(args)

if __name__ == "__main__":
    main()