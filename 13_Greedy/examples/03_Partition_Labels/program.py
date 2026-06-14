"""LC 763 - Partition Labels"""
def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    result = []
    start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result

if __name__ == "__main__":
    cases = ["ababcbacadefegdehijhklij", "eccbbbbdec", "abcd"]
    for s in cases:
        parts = partition_labels(s)
        # Show actual partitions
        idx = 0
        partitions = []
        for size in parts:
            partitions.append(s[idx:idx+size])
            idx += size
        print(f"'{s}'")
        print(f"  sizes={parts}, parts={partitions}")
