class TeliaChallenge:
    replace = {
        "NORTH": 1,
        "SOUTH": -1,
        "EAST": 2,
        "WEST": -2
    }

    replace_reversed = {v: k for k, v in replace.items()}

    # The 30 minutes way
    def pathReduc(self, arr):
        replaced = list(map(self.replace.get, arr))

        reduced = True

        # Loop while there is something to reduce.
        while reduced and len(replaced) > 1:
            for i in range(len(replaced) - 1):
                reduced = False

                if replaced[i] + replaced[i+1] == 0:
                    del replaced[i:i+2]
                    reduced = True

                    break

        return list(map(self.replace_reversed.get, replaced))
