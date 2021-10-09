import argparse
from lib.data_creator import CreateData

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest = "save_dir", type = str, required = True)
    parser.add_argument("-c", dest = "count", type = int)
    parser.add_argument("-is", dest = "image_size", type = int, default = 224)

    args = parser.parse_args()

    data_creator = CreateData(max_count = args.count, image_size =  args.image_size)
    total_count = data_creator.run(save_path_dir = args.save_dir)

    print(f"Total image {total_count} saved.")

if __name__ == "__main__":
    main()
