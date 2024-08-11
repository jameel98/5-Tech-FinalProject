from jira import JIRA

from infra.browser.browser_wrapper import BrowserWrapper


class JiraSetup:
    def __init__(self):
        self._config = BrowserWrapper().config
        self.auth_jira = JIRA(

            basic_auth=(self._config["email"], self._config["jira_api_token"]),
            options={'server': self._config["jira_url"]}
        )

    def create_issue(self, summary, description, project_key, issue_type="bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        print(f"Issue created: {new_issue.key}")
        return new_issue.key
