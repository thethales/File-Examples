import index
import metadata


def main():
    metadata.generateYMLInfoFiles()
    index.buildIndex()
    

if __name__ == "__main__":
    main()