my_dict = {"a": 1, "b": 2}

my_dict.pop("a")

my_dict["c"] = 3

my_dict.setdefault("d", 4)
my_dict.setdefault("c", 4)
my_dict.update({"a": 1, "c": 666})

del my_dict["c"]

print(my_dict)
