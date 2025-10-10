
class FieldsArray():
    def get_data(self, tab):
        try:
            if tab == "LeftNav_Level1":
                return [
                    'Home',
                    'Dashboard',
                    'Configuration',
                    'Workspace',
                    'Navigation',
                    'Tasks',
                    'Reports',
                    'Audit Logs'
                ]
            elif tab == "LeftNav_Config":
                return [
                    'Region',
                    'Country',
                    'Dropdown Value',
                    'Category',
                    'Question',
                    'Rule Set',
                    'Dependency Rule Set',
                    'Dependency Rule',
                    'Question Group',
                    'Category Question Group'
                ]
            elif tab == "LeftNav_Workspace":
                return [
                    'Repository',
                    'Permission',
                    'Quick Link',
                    'Email Templates'
                ]
            elif tab == "LeftNav_Navigation":
                return [
                    'Top Navigation',
                    'Floating Navigation'
                ]
            elif tab == "LeftNav_Tasks":
                return [
                    'My CR Tasks',
                    'All CR Tasks'
                ]
            elif tab == "LeftNav_Reports":
                return [
                    'My Reports',
                    'All Reports'
                ]
            elif tab == "LeftNav_AuditLogs":
                return [
                    'All',
                    'Repository',
                    'Task',
                    'Reports'
                ]
            elif tab == "RuleSet_Operator":
                return [
                    '=',
                    '<>',
                    '>=',
                    '>',
                    '<=',
                    '<',
                    'contains',
                    'notcontains'
                ]
            elif tab == "RuleSet_Condition":
                return [
                    'AND',
                    'OR'
                ]
        except Exception as e:
            print()
