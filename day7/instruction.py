import sys

class Tree(object):
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
    
    def find_child(self,name):
        to_search_children = self.children.copy()
        while len(to_search_children) >= 1:
            if to_search_children[0].name == name:
                return to_search_children[0]
            for child in to_search_children[0].children:
                to_search_children.append(child)
            to_search_children.remove(to_search_children[0])
        return None

    def find_leafes(self):
        to_search_children = self.children.copy()
        leafes = []
        while len(to_search_children) >= 1:
            if len(to_search_children[0].children) == 0:
                leafes.append(to_search_children[0])
            for child in to_search_children[0].children:
                to_search_children.append(child)
            to_search_children.remove(to_search_children[0])
        return leafes

    def __str__(self):
        return "Name: {}".format(self.name)
    def __repr__(self):
        return self.__str__()
    def __lt__(self, other):
        return self.name < other.name


def part_one(lines):
    print("part one")
    root = Tree("root")
    root.name="root"
    for line in lines:
        to_finish = line.split(" ")[1]
        to_begin = line.split(" ")[7]
        to_finish_node = root.find_child(to_finish)
        to_begin_node = root.find_child(to_begin)

        if to_finish_node == None:
            to_finish_node = Tree(to_finish)
        if to_begin_node is None:
            to_begin_node = Tree(to_begin)
            to_begin_node.parents.append(root)
            root.children.append(to_begin_node)
        to_finish_node.parents.append(to_begin_node)
        to_begin_node.children.append(to_finish_node)
        if root in to_finish_node.parents and len(to_finish_node.parents) >= 2:
            root.children.remove(to_finish_node)
            to_finish_node.parents.remove(root)
    while True:
        if root.find_leafes() == []:
            print("")
            break
        min_name = min(leaf.name for leaf in root.find_leafes())
        min_node = root.find_child(min_name)
        print(min_name, end="")
        for parent in min_node.parents:
            parent.children.remove(min_node)

def time(char):
    return ord(char)-4

class Worker(object):
    def __init__(self,work):
        self.time = time(work)
        self.name = work 
    def work(self):
        self.time -= 1
        if self.time <= 1:
            return "finished"
        return "still working"
    def __repr__(self):
        return "{} {}".format(self.name, self.time)

def part_two(lines):
    print("part two")
    root = Tree("root")
    root.name="root"
    for line in lines:
        to_finish = line.split(" ")[1]
        to_begin = line.split(" ")[7]
        to_finish_node = root.find_child(to_finish)
        to_begin_node = root.find_child(to_begin)

        if to_finish_node == None:
            to_finish_node = Tree(to_finish)
        if to_begin_node is None:
            to_begin_node = Tree(to_begin)
            to_begin_node.parents.append(root)
            root.children.append(to_begin_node)
        to_finish_node.parents.append(to_begin_node)
        to_begin_node.children.append(to_finish_node)
        if root in to_finish_node.parents and len(to_finish_node.parents) >= 2:
            root.children.remove(to_finish_node)
            to_finish_node.parents.remove(root)

    workers = []
    for i in range(5):
        workers.append(Worker("ß"))
        workers[i].time = 0
    worked_on = set()
    s = -1
    while True:
        s += 1
        if root.find_leafes() == []:
            print("")
            break
        avaliable_work = sorted(list(set(root.find_leafes()))) # feels cs graduade man
        
        for counter, worker in enumerate(workers):
            if worker.work() is "finished":
                delete = worker.name
                delete_node = root.find_child(delete)
                if delete is not "ß" and delete_node is not None:
                    for parent in delete_node.parents:
                        parent.children.remove(delete_node)
                for work in avaliable_work:
                    if work.name not in worked_on:
                        workers[counter] = Worker(work.name)
                        worked_on.add(work.name)
                        break
    print(s)



def main():
    input_lines = []
    if len(sys.argv) > 1:
        for line in sys.argv[1:]:
            input_lines.append(line)
    else:
        for line in sys.stdin:
            input_lines.append(line)
    part_one(input_lines)
    part_two(input_lines)

if __name__ == "__main__":
    main()
