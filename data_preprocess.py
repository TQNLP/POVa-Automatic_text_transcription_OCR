import os

def preprocess_dataset(file_path, dataset_path) :
    dataset, vocab, max_len = [], set(), 0
    sentences = open(os.path.join(file_path, "lines.txt"), "r").readlines()
    for line in sentences:
        if line.startswith("#"):
            continue

        line_split = line.split(" ")
        if line_split[1] == "err":
            continue

        folder1 = line_split[0][:3]
        folder2 = line_split[0][:8]
        file_name = line_split[0] + ".png"
        label = line_split[-1].rstrip('\n')
        print(label)
        #print(file_name)
        rel_path = os.path.join(dataset_path, folder1, folder2, file_name)
        #print(rel_path)
        if not os.path.exists(rel_path):
            #print("not found")
            continue

        dataset.append([rel_path, label])
        vocab.update(list(label))
        max_len = max(max_len, len(label))
 

if __name__ == "__main__":
    preprocess_dataset(".\\dataset\\sum_meta\\", ".\\dataset\\IAM-lines\\")

    