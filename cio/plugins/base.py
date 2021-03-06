# coding=utf-8
from __future__ import unicode_literals

from cio.conf import settings


class BasePlugin(object):

    ext = None

    @property
    def settings(self):
        return settings.get(self.ext.upper(), {})

    def load(self, content):
        """
        Return plugin data for content string
        """
        return content

    def load_node(self, node):
        """
        Return plugin data and modify for raw node
        """
        return self.load(node.content)

    def save(self, data):
        """
        Persist external plugin resources and return content string for plugin data
        """
        return data

    def save_node(self, node):
        """
        Perform action on node, persist external plugin resources and return content string for plugin data
        """
        node.content = self.save(node.content)
        return node

    def publish_node(self, node):
        """
        Perform actions on publish and return node to persist
        """
        return node

    def delete(self, data):
        """
        Delete external plugin resources
        """
        pass

    def delete_node(self, node):
        """
        Delete external plugin resources
        """
        self.delete(node.content)

    def render(self, data):
        """
        Render plugin
        """
        return data

    def render_node(self, node, data):
        """
        Prepares node for render and returns rendered content
        """
        return self.render(data)
