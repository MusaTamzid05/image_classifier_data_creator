from lib.data_creator import CreateData

def main():
    data_creator = CreateData()
    data_creator.run(save_path_dir = "./test")

if __name__ == "__main__":
    main()
