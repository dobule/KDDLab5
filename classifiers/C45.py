import math
import numpy as np
from classifiers.utils.decision_tree import *


class C45:
    def __init__(self, threshold=0.1):
        self.df = None
        self.domain = None
        self.tree = None
        self.threshold = threshold

    def entropy(self, df):
        class_counts = df.groupby(self.domain.category.name).size()
        probs = [(count / df.shape[0]) for count in class_counts]
        expressions = [(prob * math.log(prob, 2)) if prob != 0 else 0 for prob in probs]
        return - sum(expressions)
    
    def entropy_continuous(self, df, attribute, split):
        d_minus = df[df[attribute.name] <= split]
        d_minus_entropy = self.entropy(d_minus)
        d_minus_prob = d_minus.shape[0] / df.shape[0]
    
        d_plus = df[df[attribute.name] > split]
        d_plus_entropy = self.entropy(d_plus)
        d_plus_prob = d_plus.shape[0] / df.shape[0]
    
        return (d_minus_prob * d_minus_entropy) + (d_plus_prob * d_plus_entropy)
    
    def find_best_split(self, attribute, df):
        entropy = self.entropy(df)
        splits = list(np.unique(df[attribute.name]))
        attribute.values = splits
        split_entropies = [self.entropy_continuous(df, attribute, split) for split in splits]
        gains = [entropy - split_entropy for split_entropy in split_entropies]
        return splits[gains.index(max(gains))]
    
    def select_splitting_attr(self, df, attributes):
        df_len = df.shape[0]
        entropy = self.entropy(df)
        entropies = []
        binary_split_vals = []
        for attr in attributes:
            if attr.is_continuous:
                split = self.find_best_split(attr, df)
                binary_split_vals.append(split)
                entropies.append(self.entropy_continuous(df, attr, split))
            else:
                dom_vals = list(np.unique(df[attr.name]))
                splits = [df[df[attr.name] == v] for v in dom_vals]
                nrm_ratios = [split.shape[0] / df_len for split in splits]
                entropies.append(sum([(nrm_ratios[i] * self.entropy(splits[i])) for i in list(range(len(splits)))]))
    
        gains = [entropy - e for e in entropies]
        max_gain = max(gains)
        max_gain_index = gains.index(max_gain)
        best = attributes[gains.index(max(gains))]
        binary_split_val = binary_split_vals[max_gain_index] if best.is_continuous else None

        return (best, binary_split_val) if max_gain > self.threshold else (None, None)
    
    def most_freq(self, df):
        counts = df.groupby([self.domain.category.name]).size()
        maxlbl = None
        maxcount = -1
        p = None
        for lbl, count in counts.iteritems():
            if maxcount < int(count):
                maxcount = count
                maxlbl = lbl
                p = int(count) / df.shape[0]
        return maxlbl, p

    def fit(self, df, domain):
        self.df = df
        self.domain = domain
        attributes = [attribute for attribute in self.domain.attributes if attribute.name in self.df.columns.values]
        self.tree = Tree(self.build_tree(df, attributes))

    def predict(self, records):
        return [classify_record(record, self.tree.root, self.domain) for _, record in records.iterrows()]

    def build_tree(self, df, attr_list):
        outcomes = list(np.unique(df[self.domain.category.name]))
        if len(outcomes) == 1:
            val = outcomes[0]
            return Leaf(val, 1)
        elif len(attr_list) == 0:
            val, p = self.most_freq(df)
            return Leaf(val, p)
        else:
            splitting_attr, binary_split_val = self.select_splitting_attr(df, attr_list)
            if splitting_attr is None:
                val, p = self.most_freq(df)
                return Leaf(val, p)
            else:
                node = Node(splitting_attr.name)
                splits = []
                if splitting_attr.is_continuous:
                    splits.append((binary_split_val, df[df[splitting_attr.name] <= binary_split_val]))
                    splits.append((binary_split_val, df[df[splitting_attr.name] > binary_split_val]))
                else:
                    attr_list.remove(splitting_attr)
                    for val in splitting_attr.values:
                        splits.append((val, df[df[splitting_attr.name] == val]))
                for val, split in splits:
                    if not split.empty:
                        leaf = self.build_tree(split, attr_list)
                        edge = Edge(val)
                        edge.add_child(leaf)
                        node.add_child(edge)
                return node
