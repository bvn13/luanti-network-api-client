from miney.minetest import Minetest


mt = Minetest(server='bvn13.me', port=29999, playername='bvn13')

print("Connected to", mt)

for tool_type in mt.tool:
    print(tool_type)

for type in mt.node.type:
    print(type)