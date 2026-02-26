for x in range(1, 51):
    print("QuadHex" * (x % 4 == 0 and x % 6 == 0) +
          "Quad" * (x % 4 == 0 and x % 6 != 0) +
          "Hex" * (x % 6 == 0 and x % 4 != 0) or x)