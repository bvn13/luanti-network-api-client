from miney.minetest import Minetest


def build_it(mt, px, py, pz, name):
    mt.node.set(nodes={
        "x": px,
        "y": py,
        "z": pz
    }, name=name)


def build_tree(mt, px, py, pz):
    print("Building tree")
    for i in range(0, 10):
        build_it(mt, px, py + i, pz, "mcl_trees:stripped_oak")
    print("Trunk is done")
    print("Building leaves")
    for i in range(3, 11):
        print(f"Building leaves at {i}")
        volume = 12 - i
        for x in range(int(-volume / 2 - 1), int(volume / 2 + 1)):
            for z in range(int(-volume / 2 - 1), int(volume / 2 + 1)):
                if not (x == 0 and z == 0):
                    build_it(mt, px + x, py + i, pz + z, "mcl_trees:leaves_dark_oak")
    print("Leaves are done")


def main():
    mt = Minetest(server='bvn13.me', port=29999, playername='bvn13')
    print("Connected to", mt)
    players = mt.player
    if len(players):
        for player in players:
            if player.name == 'bvn13':
                pp = player.position
                px = pp["x"]
                py = pp["y"]
                pz = pp["z"]
                build_tree(mt, px + 1, py, pz + 1)
    else:
        raise Exception("There is no player with name bvn13 on server")


main()
