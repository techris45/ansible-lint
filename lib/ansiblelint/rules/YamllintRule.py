from ansiblelint.rules import AnsibleLintRule


class YamllintRule(AnsibleLintRule):
    id = 'YAML.'
    shortdesc = 'YAML'
    description = ''
    severity = 'VERY_LOW'
    tags = ['formatting']
    version_added = 'v4.3.0'

    def __init__(self, id=""):
        # customize id by adding the one reported by yamllint
        self.id = self.__class__.id + id
