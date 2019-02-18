import xml.etree.ElementTree as ET
from xml.dom import minidom
from enum import Enum, unique


@unique
class NodeType(Enum):
    TREE = 'tree'
    NODE = 'node'
    EDGE = 'edge'
    LEAF = 'leaf'


def classify_record(record, node, domain):
    if node.type == NodeType.LEAF:
        return node.choice
    elif node.type == NodeType.NODE:
        if domain.get_attribute(node.attr).is_continuous:
            left_or_right = (record[node.attr] > float(node.children[0].name))
            return classify_record(record, node.children[left_or_right].children[0], domain)
        else:
            choice = record[node.attr]
            for edge in node.children:
                if edge.name == choice:
                    return classify_record(record, edge.children[0], domain)


class Tree:
    def __init__(self, root):
        # assert root.type == NodeType.NODE
        self.root = root
        self.type = NodeType.TREE

    def as_element_tree(self):
        tree = ET.Element(NodeType.TREE.value)
        tree.append(self.root.as_element_tree())
        return tree

    @staticmethod
    def prettify(elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def to_xml(self):
        return self.prettify(self.as_element_tree())


class Node:
    def __init__(self, attr_name):
        self.attr = attr_name
        self.children = []
        self.type = NodeType.NODE

    def add_child(self, child):
        assert child.type == NodeType.EDGE
        self.children.append(child)

    def as_element_tree(self):
        node = ET.Element(NodeType.NODE.value, attrib={'var': self.attr})
        node.extend([child.as_element_tree() for child in self.children])
        return node


class Edge:
    def __init__(self, name):
        self.name = str(name)
        self.children = []
        self.type = NodeType.EDGE

    def add_child(self, child):
        assert child.type == NodeType.NODE or child.type == NodeType.LEAF
        self.children.append(child)

    def as_element_tree(self):
        node = ET.Element(NodeType.EDGE.value, attrib={'var': self.name})
        node.extend([child.as_element_tree() for child in self.children])
        return node


class Leaf:
    def __init__(self, choice, p):
        self.choice = choice
        self.p = str(p)
        self.type = NodeType.LEAF

    def as_element_tree(self):
        return ET.Element(NodeType.LEAF.value, attrib={'choice': self.choice, 'p': str(self.p)})
