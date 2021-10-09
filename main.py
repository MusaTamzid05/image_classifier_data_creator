import argparse
from lib.data_creator import CreateData

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest = "save_dir", type = str, required = True, help = "The label name of the directory")
    parser.add_argument("-c", dest = "count", type = int, help = "Total image count that should be save")
    parser.add_argument("-is", dest = "image_size", type = int, default = 224, help = "The size in which the image should saved")

    args = parser.parse_args()

    data_creator = CreateData(max_count = args.count, image_size =  args.image_size)
    total_count = data_creator.run(save_path_dir = args.save_dir)

    print(f"Total image {total_count} saved.")

if __name__ == "__main__":
    main()
