from metaflow.cards import MetaflowCard
from metaflow.plugins.cards.card_modules.test_cards import TestEditableCard


class TestNonEditableImportCard(MetaflowCard):
    type = "non_editable_import_test_card"

    ALLOW_USER_COMPONENTS = False

    def __init__(self, options=None, components=None, graph=None):
        self._options, self._components, self._graph = (
            options if options else {},
            components if components else [],
            graph,
        )

    def render(self, task):
        return task.pathspec


class TestEditableImportCard(TestEditableCard):
    type = "editable_import_test_card"

    ALLOW_USER_COMPONENTS = True


CARDS = [TestEditableImportCard, TestNonEditableImportCard]
