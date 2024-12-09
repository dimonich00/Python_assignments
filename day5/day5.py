import sys


def get_input():
    if len(sys.argv) > 1:
        all_seq = dict()
        try:
            for filename in sys.argv[1:]:
                with open(filename) as file:
                    seq = file.read()
                    all_seq[filename] = seq
        except FileNotFoundError:
            exit("Wrong filename")
    return all_seq


def data_count(data_dict):
    for key, value in data_dict.items():
        print(key)
        seq_len = len(value)
        A_count = value.count("A")
        T_count = value.count("T")
        G_count = value.count("G")
        C_count = value.count("C")
        X_count = value.count("X")

        return [A_count, T_count, G_count, C_count, X_count, seq_len]


def data_print(seq_counts):
    seq_len = seq_counts[5]
    A_count = seq_counts[0]
    T_count = seq_counts[1]
    G_count = seq_counts[2]
    C_count = seq_counts[3]
    X_count = seq_counts[4]
    print(f"A:        {A_count}    {100 * A_count/seq_len: .3f}%")
    print(f"T:        {T_count}    {100 * T_count/seq_len: .3f}%")
    print(f"G:        {G_count}    {100 * G_count/seq_len: .3f}%")
    print(f"C:        {C_count}    {100 * C_count/seq_len: .3f}%")
    print(f"Unknown:  {X_count}    {100 * X_count/seq_len: .3f}%")
    print(f"Total: {seq_len}")


if __name__ == "__main__":
    saved_seqs = get_input()
    calculated_data = data_count(saved_seqs)
    data_print(calculated_data)
