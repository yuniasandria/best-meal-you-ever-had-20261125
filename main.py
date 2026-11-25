import os

SENTENCE = "After a 14-hour night shift I came home at 2 a.m. to grandma's chicken soup — three meatballs, one soft egg, steam fogging my glasses — and ate it standing because her kitchen chair was broken."

# PART_A

# PART_B
def main():
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.strip() == SENTENCE
    assert SENTENCE.count(".") == 3
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
