from __future__ import absolute_import
import unittest
import dynetx as dn
import os


class ReadWriteTestCase(unittest.TestCase):

    def test_snapshots(self):
        g = dn.DynGraph()
        g.add_interaction(1, 2, 2)
        g.add_interaction(1, 2, 2, e=6)
        g.add_interaction(1, 2, 7, e=11)
        g.add_interaction(1, 2, 8, e=15)
        g.add_interaction(1, 2, 18)
        g.add_interaction(1, 2, 19)
        dn.write_snapshots(g, "test.txt", delimiter=" ")
        h = dn.read_snapshots("test.txt", nodetype=int, timestamptype=int)
        self.assertEqual(g.number_of_interactions(), h.number_of_interactions())
        self.assertEqual(list(g.stream_interactions()), list(h.stream_interactions()))
        os.remove("test.txt")

    def test_interaction_graph(self):
        g = dn.DynGraph()
        g.add_interaction(1, 2, 2)
        g.add_interaction(1, 2, 2, e=6)
        g.add_interaction(1, 2, 7, e=11)
        g.add_interaction(1, 2, 8, e=15)
        g.add_interaction(1, 2, 18)
        g.add_interaction(1, 2, 19)
        dn.write_interactions(g, "test2.txt", delimiter=" ")
        h = dn.read_interactions("test2.txt", nodetype=int, timestamptype=int)
        self.assertEqual(list(g.stream_interactions()), list(h.stream_interactions()))
        self.assertEqual(g.number_of_interactions(), h.number_of_interactions())
        os.remove("test2.txt")

    def test_interaction_graph_flag(self):
        g = dn.DynGraph()
        g.add_interaction(1, 2, 2)
        g.add_interaction(1, 2, 2, e=6)
        g.add_interaction(1, 2, 7, e=11)
        g.add_interaction(1, 2, 8, e=15)
        g.add_interaction(1, 2, 18)
        g.add_interaction(1, 2, 19)
        dn.write_interactions(g, "test3.txt", delimiter=" ")
        h = dn.read_interactions("test3.txt", nodetype=int, timestamptype=int, keys=True)
        # self.assertEqual(list(g.stream_interactions()), list(h.stream_interactions()))
        self.assertEqual(g.number_of_interactions(), h.number_of_interactions())
        os.remove("test3.txt")

    def test_snapshot_graph_flag(self):
        g = dn.DynGraph()
        g.add_interaction(1, 2, 2)
        g.add_interaction(1, 2, 2, e=6)
        g.add_interaction(1, 2, 7, e=11)
        g.add_interaction(1, 2, 8, e=15)
        g.add_interaction(1, 2, 18)
        g.add_interaction(1, 2, 19)
        dn.write_snapshots(g, "test4.txt", delimiter=" ")
        h = dn.read_snapshots("test4.txt", nodetype=int, timestamptype=int, keys=True)
        # self.assertEqual(list(g.stream_interactions()), list(h.stream_interactions()))
        self.assertEqual(g.number_of_interactions(), h.number_of_interactions())
        os.remove("test4.txt")



if __name__ == '__main__':
    unittest.main()
