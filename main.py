import helper


def main():
    print("1. Single Page [Appends at singleDatas.json]")
    print("2. Tailored Clothes (All) [Saves as tailoredData.json]")
    print("3. Featured Products (All) [Saves as featuredProducts.json]")
    print("4. bla bla [Does't work]")
    inp = int(input("Your Choice: "))
    if inp == 1:
        helper.SingleScrap()
    elif inp == 2:
        helper.GetTailoredCloth()
    elif inp == 3:
        helper.GetAllFeaturedProducts()
    else:
        print("Other option doesn't work properly. Please have a look at the code file.")


if __name__ == "__main__":
    main()
