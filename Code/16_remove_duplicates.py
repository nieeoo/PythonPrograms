def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))

if __name__ == "__main__":
    print(remove_duplicates([1,2,2,2,3,3,4,4,5,5,1,4]))